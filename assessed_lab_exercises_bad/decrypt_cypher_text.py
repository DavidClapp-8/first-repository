def decrypt_cypher_text(encrypted_text, key):
    #function implementation here...
    decrypted_text = ""
    for i in encrypted_text:
        encrypted_text_ord = ord(i)
        diff = encrypted_text_ord - key
        remainder = diff % 256
        decrypted_text += (chr(remainder))

    return decrypted_text
print(decrypt_cypher_text("Hdfk#huuru#|rx#pdnh#lq#surjudpplqj#lv#dq#rssruwxqlw|#wr#ehfrph#d#ehwwhu#ghyhorshu$", 3))