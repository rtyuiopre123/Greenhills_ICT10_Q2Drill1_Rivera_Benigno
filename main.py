from pyscript import document

def trapezoid_formula(event):
    factor1 = float(document.getElementById("baseA").value or 0)
    factor2 = float(document.getElementById("baseB").value or 0)
    factor3 = float(document.getElementById("height").value or 0)

    area = (factor1 + factor2) / 2 * factor3

    document.getElementById("result").innerText = (
        f"If the bases are {factor1} & {factor2}, and the height is {factor3}, "
        f"the area of the trapezoid is {area}."
    )

button = document.getElementById("calc-btn")
button.addEventListener("click", trapezoid_formula)
