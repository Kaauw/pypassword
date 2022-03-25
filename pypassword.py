import secrets
import hashlib
from passlib.hash import sha512_crypt
class Password:
    """
    Password Class

    Attributes
    ----------
        lenght (int, optional): Password lenght. Defaults to 16.

        
    """
    def __init__(self, lenght: int = 16):
        """Construct Password Object using attributes described bellow 
        Args:
            lenght (int, optional): Password lenght. Defaults to 16.
        """
        self.lenght = lenght
    def generate(self) -> str:
        """Password generation algorithm

        Returns:
            str: generated password string
        """
        
        password = []
        lower_char = ('a','b','c','d','e','f','g','h','i','j','k','m','n','o','q','r','s','t','u','v','w','x','y','z')
        upper_char = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','Q','R','S','T','U','V','W','X','Y','Z') 
        numbers = ('1','2','3','4','5','6','7','8','9','0')
        specials = ('@','&',';',',','#','*')

        for i in list(range(self.lenght)):
            rand_char = secrets.choice(list(range(1, 5)))
            if rand_char == 1:
                password.append(secrets.choice(lower_char))
            elif rand_char == 2:
                password.append(secrets.choice(upper_char))
            elif rand_char == 3:
                password.append(secrets.choice(numbers))
            elif rand_char == 4:
                password.append(secrets.choice(specials))

        self.password = "".join(password)

    def getpass(self) -> dict:
        """Return a dict with password as plain text, md5 and sha256 hashes

        Returns:
            dict: {'plain_text': value, 'md5': value; 'sha256': value, 'sha512_crypt': value}
        """
        return {'plain_text': self.password, 'md5': self.getpass_md5(), 'sha256': self.getpass_sha256(), 'sha512_crypt' : self.getpass_sha512_crypt()}

    def getpass_plain_text(self) -> str:
        """Return a string with plain text password

        Returns:
            str: Plain text password
        """
        return self.password

    def getpass_md5(self) -> str:
        """Return a string with md5 hashed password

        Returns:
            str: md5 hashed password
        """
        return hashlib.md5(self.password.encode()).hexdigest()

    def getpass_sha256(self) -> str:
        """Return a string with sha256 hashed password

        Returns:
            str: sha256 hashed password
        """
        return hashlib.sha256(self.password.encode()).hexdigest()

    def getpass_sha512_crypt(self) -> str:
        """Return a string with sha512_crypt ($6$) encrypted password

        Returns:
            str: sha512 encrypted password
        """
        return sha512_crypt.hash(self.password.encode())
if __name__ == "__main__":
    print(Password.__doc__)