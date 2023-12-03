import PIL
from sys import argv


class Compressor:
    def __init__(self, mode: str, filename: str) -> None:
        self.filename = filename
        self.mode = mode
    
        if self.mode == "compress":
            self.compression()
        else:
            self.decompression()
            
            
    def read_content_from_image(self):
        """
        La funzione apre l'immagine e legge i valori dei pixel riscrivendoli, riga per riga,  
        in base alla risoluzione dell'immagine stessa. Successivamente chiama la funzione 'compress()'.
        """
        pass
    
    
    def read_content_from_file(self):
        """
        La funzione apre il file dove sono stati sintetizzati i valori dei pixel dell'immagine 
        e li formatta in tuple che poi saranno inserite in liste. Successivamente chiama la funzione 'decompress()'
        """
        pass
    
    
    def compression(self):
        """
        Dati i valori dei pixel, la funzione li 'sintetizza' scrivendo, in una lista, 
        il numero di volte che si ripetono e il valore che hanno in comune. 
        """
        
    
    def compression_optimization(self):
        """
        Finita la prima parte della compressione, la funzione riscrive i valori in un file di testo, 
        eliminando tutti gli elementi caratteristici della sintassi delle liste e delle tuple di Python, 
        riducendo notevolmente la dimensione del file.
        """
        pass
    
    
    def decompression(self):
        """Dopo aver letto il file contenete i valori sintetizzati dei pixel, la funzione li riformatta in liste."""
        pass
    
    
    def decompression_optimization(self):
        """Dopo la prima fase della decompressione dell'immagine, la funzione legge i valori dei pixel e ricompone l'immagine."""
        pass
    
    

def usage(error: str | None) -> str:
    """Restituisce la lista dei comandi disponibili."""

    if error != None:
        print(f"Error: {error}")
    print("\nUSAGE:")
    print("\t- python ImageCompressor.py compress FILENAME    -   compress an image")
    print("\t- python ImageCompressor.py decompress FILENAME  -   decompress an image\n")
    exit(0)



if __name__ == "__main__":
    match len(argv):
        case 1:
            usage(error=None)
        case 2:
            usage(error="not enough arguments were passed.")
        case 3:
            if argv[1] == "compress":
                Compressor(mode="compress", filename=argv[2])
            elif argv[1] == "compress":
                Compressor(mode="decompress", filename=argv[2])
            else:
                usage(error=f"uknown command \"{argv[1]}\".")
        case _:
            usage(error="too many arguments were passed.")
