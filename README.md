# 🔐 String Hasher & Encoder

A simple and lightweight Python CLI tool for generating cryptographic hashes and encoding strings into multiple formats.

> **Note:** This repository is an updated and modified version of the original project by **bl4de**. I did not create the original project; I updated and improved the existing code.

---

## 🇹🇷 Türkçe

### 📌 Proje Hakkında

**String Hasher & Encoder**, girilen bir metni farklı hash algoritmalarıyla hesaplayan ve çeşitli encoding formatlarına dönüştüren basit bir Python komut satırı aracıdır.

Bu repository, **bl4de tarafından geliştirilen orijinal projenin tarafımdan güncellenmiş ve düzenlenmiş sürümüdür.**

### ✨ Özellikler

#### 🔑 Hash Algoritmaları

Araç aşağıdaki algoritmaları destekler:

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* BLAKE2s
* BLAKE2b

#### 🔄 Encoding

Girilen metin aşağıdaki formatlara dönüştürülebilir:

* Base64
* HEX
* URL Encoding

### 🛠️ Güncellemeler

Orijinal proje temel alınarak aşağıdaki güncellemeler ve düzenlemeler yapılmıştır:

* HEX encoding implementasyonu düzeltildi.
* Windows ANSI renk desteği eklendi/düzeltildi.
* Terminal renkleri iyileştirildi.
* Komut satırı argümanı ile kullanım desteklendi.
* Programın çift tıklayarak çalıştırılabilmesi için bekleme desteği eklendi.
* Hatalı veya desteklenmeyen hash işlemlerinde programın devam etmesi sağlandı.

HEX encoding için kullanılan güncellenmiş implementasyon `binascii.hexlify()` üzerinden yapılmaktadır.

Windows üzerinde ANSI renk işleme desteği de etkinleştirilmiştir.

### 📋 Gereksinimler

* Python 3.x
* Windows / Linux / macOS

Proje yalnızca Python standart kütüphanelerini kullanır ve harici bir Python paketi gerektirmez.

Kullanılan temel modüller:

```text
sys
os
hashlib
base64
binascii
urllib.parse
```

### 🚀 Kurulum

Repository'yi klonlayın:

```bash
git clone https://github.com/YOUR_USERNAME/string-hasher-encoder.git
```

Proje klasörüne girin:

```bash
cd string-hasher-encoder
```

Aracı çalıştırın:

```bash
python hasher.py
```

### 💻 Kullanım

Programı herhangi bir argüman vermeden çalıştırırsanız sizden bir metin girmeniz istenir:

```text
Hashlenecek metni girin:
```

Örneğin:

```text
Hashlenecek metni girin: Hello World
```

Program ardından hash ve encoding sonuçlarını gösterir.

### ⚡ Komut Satırından Kullanım

Metni doğrudan komut satırından da gönderebilirsiniz:

```bash
python hasher.py "Hello World"
```

Program tek bir komut satırı argümanı algıladığında doğrudan bu metni işler.

### 🖥️ Windows

Windows üzerinde terminal renklerinin düzgün çalışabilmesi için ANSI escape processing etkinleştirilmiştir.

Program ayrıca `.py` dosyasına çift tıklayarak çalıştırıldığında terminalin hemen kapanmaması için bekleme desteğine sahiptir.

### 📤 Örnek Çıktı

```text
HASHES:
md5             <hash>
sha1            <hash>
sha224          <hash>
sha256          <hash>
sha384          <hash>
sha512          <hash>
blake2s         <hash>
blake2b         <hash>

ENCODE:
Base64          <encoded value>
HEX encoded     <encoded value>
URL encoded     <encoded value>
```

### ⚠️ Güvenlik Uyarısı

Bu araç hash ve encoding işlemlerini gerçekleştirmek için hazırlanmıştır.

**MD5 ve SHA-1, modern parola saklama sistemleri için uygun değildir.** Hassas uygulamalarda amaca uygun, modern ve güvenli parola hashleme yöntemleri kullanılmalıdır.

---

# 🇬🇧 English

## 📌 About

**String Hasher & Encoder** is a simple and lightweight Python command-line tool for generating hashes and encoding strings into multiple formats.

This repository is an **updated and modified version of the original project created by bl4de**.

I did **not** create the original project. The original code was updated, modified, and improved for this repository.

## ✨ Features

### 🔑 Hash Algorithms

The tool supports:

* MD5
* SHA-1
* SHA-224
* SHA-256
* SHA-384
* SHA-512
* BLAKE2s
* BLAKE2b

### 🔄 Encoding

Supported encoding formats:

* Base64
* HEX
* URL Encoding

## 🛠️ Updates

The original project was updated and modified with the following changes:

* Fixed the HEX encoding implementation.
* Added/improved Windows ANSI color support.
* Improved terminal output colors.
* Added command-line argument support.
* Added support for keeping the terminal open when launched by double-clicking.
* Improved handling of unsupported or failed hash operations.

The HEX encoding implementation was corrected using `binascii.hexlify()`.

Windows ANSI escape processing is also enabled for better terminal color support.

## 📋 Requirements

* Python 3.x
* Windows / Linux / macOS

The project uses Python's standard library and does not require external Python packages.

Main modules used:

```text
sys
os
hashlib
base64
binascii
urllib.parse
```

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/string-hasher-encoder.git
```

Enter the project directory:

```bash
cd string-hasher-encoder
```

Run the tool:

```bash
python hasher.py
```

## 💻 Usage

Run the program without arguments:

```bash
python hasher.py
```

You will be asked to enter a string:

```text
Hashlenecek metni girin:
```

You can also provide the string directly:

```bash
python hasher.py "Hello World"
```

When a command-line argument is provided, the program processes it directly.

## 🖥️ Windows Support

Windows ANSI escape processing is enabled to provide colored terminal output.

The program also includes a pause mechanism so the terminal does not immediately close when the Python file is launched by double-clicking.

## 📤 Example Output

```text
HASHES:
md5             <hash>
sha1            <hash>
sha224          <hash>
sha256          <hash>
sha384          <hash>
sha512          <hash>
blake2s         <hash>
blake2b         <hash>

ENCODE:
Base64          <encoded value>
HEX encoded     <encoded value>
URL encoded     <encoded value>
```

## ⚠️ Security Notice

This tool is intended for hashing and encoding purposes.

**MD5 and SHA-1 should not be used for modern password storage.** For sensitive applications, use appropriate modern password-hashing algorithms and security practices.

---

# 👤 Credits & Attribution

### Original Project

This project is based on the original work of **bl4de**.

* **Original Author:** [bl4de](https://github.com/bl4de)
* **Original Source:** `github.com/bl4de`
* **Original File:** `hasher.py`

The original author is identified directly in the source code.

### Updated Version

* **Updated by:** FoxTR
* **Updated:** 2026
* **Type:** Updated / Modified Version

This repository is **not presented as the original work**. It is a modified and updated version of the original project.

---

# 📁 Project Structure

```text
string-hasher-encoder/
│
├── hasher.py
├── README.md
├── LICENSE
└── requirements.txt
```

---

# 📜 License

Please refer to the `LICENSE` file included in this repository for the applicable license and redistribution terms.

The original project's license and attribution requirements should be respected when redistributing or modifying the code.

---

# ⭐ Support

If you find this updated version useful, consider giving the repository a ⭐ star.

**Original project:** `github.com/bl4de`

**Updated version:** FoxTR — 2026
