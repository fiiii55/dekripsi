def dekripsi(teks_enkripsi, a, b):
  """
  Fungsi untuk mendekripsi teks yang dienkripsi menggunakan Affine Cipher.

  Args:
    teks_enkripsi: Teks terenkripsi yang ingin didekripsi.
    a: Nilai 'a' dalam rumus Affine Cipher.
    b: Nilai 'b' dalam rumus Affine Cipher.

  Returns:
    Teks asli.
  """
  teks_enkripsi = teks_enkripsi.upper()

  teks_asli = ""

  for char in teks_enkripsi:

    angka_char = ord(char) - ord('A')

    angka_dekripsi = a**-1 * (angka_char - b) % 26

    char_asli = chr(angka_dekripsi + ord('A'))

    teks_asli += char_asli

  return teks_asli
