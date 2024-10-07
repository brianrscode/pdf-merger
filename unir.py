import sys
import os
import PyPDF2


ruta_actual = os.getcwd()

def existen_pdfs(lista_pdfs:list[str]):
    """Verifica si existen los PDF's que se pasaron como parámetros"""
    return all(os.path.exists(os.path.join(ruta_actual, pdf)) for pdf in lista_pdfs)


def unir_pdfs(lista_pdfs:list[str], nombre_pdf_salida:str):
    """Unir los PDF's que se pasaron como parámetros"""
    try:
        pdf_final = PyPDF2.PdfMerger()
        for archivo in lista_pdfs:
            pdf_final.append(archivo)

        pdf_final.write(nombre_pdf_salida)
        pdf_final.close()
    except Exception as e:
        print(f"Hubo un error al unir los PDF's: {lista_pdfs[:]}\n{e}")
    else:
        print("Los PDF's se unieron correctamente")


def main() -> None:
    nombre_pdf_salida:str = sys.argv[1]
    lista_pdfs:list = sys.argv[2:]

    if(len(lista_pdfs) < 2):
        print("Debes de agregar al menos 2 PDF's para unir")
        return

    if not existen_pdfs(lista_pdfs):
        print("No existen los PDF's que se pasaron como parámetros")
        return

    if not nombre_pdf_salida.endswith(".pdf"):
        nombre_pdf_salida += ".pdf"

    unir_pdfs(lista_pdfs, nombre_pdf_salida)


if __name__ == "__main__":
    main()
