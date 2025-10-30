from RSA import encrypt, decrypt, generate_keypair

p, q = 3557, 2579
public, private = generate_keypair(p, q)
plaintext = "Hello World!"

array = [1830186, 474009, 2963946, 2963946, 7480127, 16951, 3508237, 7480127, 1582356, 2963946, 6388304, 8264997]
c = (2152519, 9173503)

print(decrypt(c, array))

