class User:


    def __init__(self):
        self.DNI = ""
        self.PhoneNumber = ""
        self.Email = ""
        self.Name = ""
        self.PostalAdress = ""
      

    def DadesUsuari(self,name,dni,DirPostal,phonenumber,email):
        self.DNI = dni
        self.PhoneNumber = phonenumber
        self.Email = email
        self.Name = name
        self.PostalAdress = DirPostal