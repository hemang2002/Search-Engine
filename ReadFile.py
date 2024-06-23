import PyPDF2
import os

class ReadFile:

    def __init__(self, file_path, filename):

        self.file_path = os.path.join(file_path, filename)
        self.extension = self.getExtension()


    def getExtension(self):
        return self.file_path.split(".")[-1].lower()


    def OpenFile(self):
        
        documents = []
        text = ""

        if self.extension == 'pdf':
            
            with open(self.file_path, 'rb') as f:

                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    documents.append(page.extract_text())
                    text += page.extract_text()
            f.close()
            return documents, text

        elif self.extension == 'txt':

            with open(self.file_path, "r") as f:
                
                for page in f:
                    documents.append(page)
                    text += page
            f.close()
            return documents, text

        else:
            return None, None