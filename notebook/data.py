import pandas as pd

data = pd.read_csv("KR_Superstore_sample_2025.csv")

data.columns = [
    "order_id", "order_date", "ship_date", "ship_mode",
    "customer_id", "customer_name", "segment",
    "city", "state", "country",
    "product_id", "category", "sub_category", "product_name",
    "manager", "returned",
    "sales", "quantity", "discount", "profit"
]

# 2. DICCIONARIOS, segmentos de cliente
segment_map = {
    "소비자": "Consumer",
    "기업 고객": "Corporate",
    "홈 오피스": "Home Office"
}

data["segment"] = data["segment"].replace(segment_map)


# Metodos de envio 
ship_mode_map = {
    "표준 배송": "Standard Class",
    "특급 배송": "First Class",
    "당일 배송": "Same Day",
    "빠른 배송": "Second Class"
}

data["ship_mode"] = data["ship_mode"].replace(ship_mode_map)

# Categorias 
category_map = {
    "사무용품": "Office Supplies",
    "사무기기": "Technology",
    "가구": "Furniture"
}

data["category"] = data["category"].replace(category_map)

# Subcategorías 
sub_category_map = {
    "가전": "Appliances",
    "복사기": "Copiers",
    "일반 사무용품": "Supplies",
    "종이": "Paper",
    "전산기기": "Machines",
    "탁자": "Tables",
    "필기구": "Art",
    "수납용품": "Storage",
    "의자": "Chairs",
    "바인더": "Binders",
    "가구류": "Furnishings",
    "책장": "Bookcases",
    "봉투": "Envelopes",
    "라벨": "Labels",
    "악세사리": "Accessories",
    "전화기": "Phones",
    "파스너": "Fasteners"
}

data["sub_category"] = data["sub_category"].replace(sub_category_map)

# Valores True
data["returned"] = data["returned"].astype(str).str.replace("\x08", "")
data["returned"] = data["returned"].replace({"True": True, "False": False})

# Fechas
data["order_date"] = pd.to_datetime(data["order_date"])
data["ship_date"] = pd.to_datetime(data["ship_date"])


# Ventas por categoría
data.groupby("category")["sales"].sum()

# Profit por categoría
data.groupby("category")["profit"].sum()

# Impacto del descuento
data.groupby("discount")["profit"].mean()


print(data.head())