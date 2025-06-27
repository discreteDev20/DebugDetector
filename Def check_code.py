def check_code(code):  
    errors = []  # ✅ Data structure (list)  
    try:  
        compile(code, '<string>', 'exec')  
        errors.append("✅ No syntax errors!")  
    except SyntaxError as e:  
        errors.append(f"❌ Line {e.lineno}: {e.msg}")  
    except Exception as e:  
        errors.append(f" Runtime error: {str(e)}")  
    return errors  

def save_errors(errors):  # ✅ File writing  
    with open("errors.txt", "w") as f:  
        for error in errors:  # ✅ Loop  
            f.write(error + "\n")  

def load_code():  # ✅ File reading  
    with open("user_code.py", "r") as f:  
        return f.read()  

# ✅ Conditional (if-else)  
if __name__ == "__main__":  
    code = load_code()  
    errors = check_code(code)  
    save_errors(errors)  
    print("Errors saved to errors.txt!")  