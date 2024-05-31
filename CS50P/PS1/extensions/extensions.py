file = input("File name: ").split(".")

match file[-1]:
    case "gif":
        print("")
    case "jpg":
        print("")
    case "jpeg":
        print("")
    case "png":
        print("")
    case "pdf":
        print("")
    case "txt":
        print("")
    case "zip":
        print("")
    case _:
        print("application/octet-stream")
