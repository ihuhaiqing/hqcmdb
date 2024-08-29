import base64
import rsa

def generate_keys():
    public_key, private_key = rsa.newkeys(1024)
    with open('public.pem', 'wb') as pub_file:
        pub_file.write(public_key.save_pkcs1())
    with open('private.pem', 'wb') as pri_file:
        pri_file.write(private_key.save_pkcs1())

def rsa_encrypt(data, pub_key_path='public.pem'):
    with open(pub_key_path, 'rb') as pub_file:
        public_key = rsa.PublicKey.load_pkcs1(pub_file.read())
    encrypted_data = rsa.encrypt(data.encode('utf-8'), public_key)
    return base64.b64encode(encrypted_data).decode('utf-8')

def rsa_decrypt(encrypted_data, pri_key_path='private.pem'):
    with open(pri_key_path, 'rb') as pri_file:
        private_key = rsa.PrivateKey.load_pkcs1(pri_file.read())
    decrypted_data = rsa.decrypt(base64.b64decode(encrypted_data), private_key)
    return decrypted_data.decode('utf-8')
