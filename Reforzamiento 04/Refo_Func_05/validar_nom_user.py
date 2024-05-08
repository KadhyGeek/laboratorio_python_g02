def usuario():
    nomuser = input("Ingrese el nombre de usuario: ")
    caracter = len(nomuser)
    try:
        if nomuser.isalnum() ==True:
            if caracter < 6:
                return "ERROR: El nombre de usuario debe contener al menos 7 caracteres"
            elif caracter > 13:
                return "ERROR: El nombre de usuario no puede contener más de 12 caracteres"
            else:
                return nomuser.isalnum()
    except ValueError:
        return "ERROR: El nombre de usuario puede contener solo letras y números"


usuario()
