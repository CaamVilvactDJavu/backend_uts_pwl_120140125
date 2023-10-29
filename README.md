# UTS Pemrograman Web Lanjut BackEnd

- Nama : Ilham Fadhlur Rahman
- Nim : 120140125
- Program Studi : Teknik Informatika
- Kelas : Pemrograman Web Lanjut

## Cara menjalankan aplikasi

1. Clone repository ini 

```
git clone https://github.com/CaamVilvactDJavu/backend_uts_pwl_120140125.git
```

2. Ganti ke directory pada repository ini

```
cd backend_uts_pwl_120140125 
```

### Server

1. Ganti ke Directory Server 

```
cd server
```

2. Install Virtual Environment

```
python3 -m venv env
```

3. Aktifkan Virtual Environment

```
env\Scripts\activate
```

4. Install Dependencies dan Update pip

```
python -m pip install --upgrade pip setuptools
```

```
pip install -e .
```

5. Generate gRPC 

```
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/products.proto
```

6. Buat Database

```
Buat database (mysql) dengan nama backend_uts_ilham 
```

7. Migrate Database

```
alembic upgrade head
```

8. Jalankan gRPC Server

```
python -m server
```

### Client

1. Ganti ke Directory Client

```
cd client
```

2. Install Virtual Environment

```
python3 -m venv env
```

3. Aktifkan Virtual Environment

```
env\Scripts\activate
```

4. Install Dependencies dan Update pip

```
python -m pip install --upgrade pip setuptools
```

```
pip install -e .
```

5. Generate gRPC 

```
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/products.proto
```

6. Jalankan gRPC Client

```
pserve development.ini --reload
```
