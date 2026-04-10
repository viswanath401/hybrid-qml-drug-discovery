from flask import Flask, render_template, request
import pickle
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem.rdMolDescriptors import CalcMolFormula
import requests

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

# Convert SMILES → features + formula
def smiles_to_features(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None, None

    fp = AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=128)

    # IMPORTANT FIX: ensure correct datatype
    features = np.array(fp, dtype=np.float32).reshape(1, -1)

    formula = CalcMolFormula(mol)

    return features, formula

# Fetch molecule name from PubChem
def get_molecule_name(smiles):
    try:
        url = f"https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/{smiles}/property/IUPACName/JSON"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data['PropertyTable']['Properties'][0]['IUPACName']
        else:
            return "Name not found"
    except:
        return "Name not found"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        smiles = request.form["smiles"]

        features, formula = smiles_to_features(smiles)

        if features is not None:
            # Prediction
            pred = model.predict(features)[0]

            # Probability (FIXED)
            probs = model.predict_proba(features)
            prob = float(probs[0][1])

            name = get_molecule_name(smiles)

            result = {
                "prediction": "Toxic" if pred == 1 else "Non-Toxic",
                "probability": round(prob, 4),
                "formula": formula,
                "name": name
            }
        else:
            result = {
                "prediction": "Invalid SMILES",
                "probability": "-",
                "formula": "-",
                "name": "-"
            }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)