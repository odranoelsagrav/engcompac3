import os
from flask import Flask

app = Flask(__name__)

@app.route('/')

def nao_entre_em_panico():
    limit = 100
    primos_showed = 2
    n = 4
    primos = "2, 3, "
    while primos_showed < limit:
        eh_primo = True
        for i in range(2, n):
            if n % i == 0:
                eh_primo = False
                break
        if eh_primo:
            primos += f"{n}, " if (primos_showed < limit - 1) else f"{n}."
            primos_showed += 1
        n += 1
    return primos


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

