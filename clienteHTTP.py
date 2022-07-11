
import requests
import sys

if __name__ == "__main__":

    # --------------argumentos recebidos ------------------
    arquivo = str(sys.argv[3]).replace(".html", "")
    porta = sys.argv[2]
    if(porta != "80"):
        print("Ops!!! só é possivel conectar na porta 80 ")
        exit(-1)
    ip = str(sys.argv[1])
    # -----------------------------------------------------

    # ------------conectando ao servidor-------------------------------------------------------
    try:
        msgRecebida = requests.get("http://" + ip + "/" + arquivo + ".html")
        print("Conectado no servidor")
        print(msgRecebida.text)
    except:
        print("Não foi possível conectar-se a esta rede")
    # -----------------------------------------------------------------------------------------


