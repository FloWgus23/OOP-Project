import streamlit as st
import pandas as pd
from PIL import Image

if st.sidebar.button('เกร็ดความรู้'):
    
    # กำหนดสีพื้นหลังของแถบ
    color_code = "#E07A5F"  # รหัสสี HEX

    write_html = f"""
        <style>
            .write-container {{
                background-color: {color_code};
                padding: 10px;
                text-align: center;
                width: 150%;  /* ปรับความกว้างตามที่คุณต้องการ */
                margin: auto;  /* จัดตำแหน่งกลางหน้าจอ */
            }}
            .write {{
                color: white;
            }}
        </style>
        <div class="write-container">
            <h1 class="write">บทความ: การเลือกปุ่มของรองเท้าฟุตบอล</h1>
        </div>
    """

    st.markdown(write_html, unsafe_allow_html=True)
    
    st.write("เมื่อพูดถึงรองเท้าที่ใช้ในการเตะฟุตบอล รองเท้าฟุตบอลนั้นจะมีปุ่มอยู่หลายประเภท มาดูกันเลย")

    # เขียนรายละเอียดของบทความ
    st.markdown("""
    ### ประเภทของปุ่ม:
    1. FG (Firm Ground)
    2. TF (Turf)
    3. IC (Indoor)
    4. SG (Soft Ground)
    5. AG (Artificial Grass)

    """)

    # เริ่มต้นเปลี่ยนแปลงเล็กน้อยที่นี่
    st.write("### รูปประเภทของปุ่ม")
    col1, col2, col3, col4, col5 = st.columns(5)
    
    # สร้าง URL สำหรับแต่ละประเภท
    img_urls = [
        "https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/3/230699_nike-phantom-gx-pro-df-gras-voetbalschoenen-fg-zwart-blauw_1.jpg",
        "https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/3/233615_nike-zoom-mercurial-vapor-15-academy-turf-voetbalschoenen-tf-wit-felrood-zwart.jpg",
        "https://static.nike.com/a/images/t_PDP_1728_v1/f_auto,q_auto:eco/1e90306f-67b7-442c-88f5-3c11e96c4d9b/รองเท้าฟุตบอลสำหรับสนามในร่ม-คอร์ท-phantom-gt2-club-ic-CRZfFM.png",
        "https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/4/240655_nike-premier-iii-ijzeren-nop-voetbalschoenen-sg-anti-clog-zilver-zwart.jpg",
        "https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/4/245137_nike-tiempo-legend-10-elite-kunstgras-voetbalschoenen-ag-zwart-blauw.jpg",
    ]

    # แสดงรูปภาพ
    for i, img_url in enumerate(img_urls):
        col = eval(f"col{i + 1}")
        col.image(img_url, caption=f"ปุ่ม {i + 1}", use_column_width=True)

    # สรุป
    st.markdown("""
    เมื่อเลือกรองเท้าฟุตบอล ควรพิจารณาประเภทของปุ่มที่เหมาะสมกับพื้นสนามที่จะใช้เล่น เช่น
    - FG (Firm Ground): สำหรับสนามแข็ง
    - TF (Turf): สำหรับสนามหญ้าเทียม
    - IC (Indoor): สำหรับใช้ในร่มหรือสนามภายใน
    - SG (Soft Ground): สำหรับสนามนุ่ม
    - AG (Artificial Grass): สำหรับสนามหญ้าเทียม
    """)

    # สรุป
    st.write("สรุป: การเลือกปุ่มของรองเท้าฟุตบอลมีความสำคัญเพื่อให้มีประสิทธิภาพในการใช้งานที่สูงสุด")
    video_url = "https://www.youtube.com/watch?v=jwa3xJTYvXs"
    st.video(video_url)

if st.sidebar.button('ข้อมูลเพิ่มเติม'):
    
    
    # กำหนดสีพื้นหลังของแถบ
    color_code = "#E07A5F"  # รหัสสี HEX

    write_html = f"""
        <style>
            .write-container {{
                background-color: {color_code};
                padding: 10px;
                text-align: center;
                width: 80%;  /* ปรับความกว้างตามที่คุณต้องการ */
                margin: auto;  /* จัดตำแหน่งกลางหน้าจอ */
            }}
            .write {{
                color: white;
            }}
        </style>
        <div class="write-container">
            <h1 class="write"> ข้อมูลเกี่ยวกับแบรนด์ </h1>
        </div>
    """

    st.markdown(write_html, unsafe_allow_html=True) 
    
# URL ของรูปภาพ
    image_url = "https://upload.wikimedia.org/wikipedia/commons/3/35/Nike_White_Logo_2.png"  # แทนที่ด้วย URL ของรูปภาพที่คุณต้องการใช้

    # แสดงรูปภาพ
    st.image(image_url ,  use_column_width=True)
     
    st.title('ไนกี้(Nike)นี่คือข้อมูลเกี่ยวกับแบรนด์นี้:')
     
    st.markdown("""
    -ประวัติและกำเนิด:
    - ไนกี้ (Nike, Inc.) ก่อตั้งขึ้นในปี 1964 โดยบิล ไนท์ (Bill Bowerman) และฟิล ไนท์ (Phil Knight).
    - ความเริ่ดเร็วของแบรนด์เริ่มต้นจากการผลิตรองเท้ากีฬา.
    
    -โลโก้:
    - โลโก้ของไนกี้เป็นเครื่องตราหูหนู (Swoosh), ซึ่งเป็นหนึ่งในสัญลักษณ์ที่แสดงให้เห็นว่าเป็นแบรนด์ Nike.
    
    -ผลิตภัณฑ์:
    - ไนกี้มีการผลิตและจำหน่ายรองเท้ากีฬา, เสื้อผ้า, อุปกรณ์กีฬา, และสินค้าที่เกี่ยวข้อง.
    - ผลิตภัณฑ์ของ Nike มีความหลากหลายและให้ความสำคัญกับการพัฒนาเทคโนโลยีที่ทันสมัย.
    
    -ทรัพยากรสร้างสรรค์:
    - ไนกี้มีคอลเล็กชั่นสัญชาติอย่าง Air Jordan ที่ได้รับความนิยมมาก.
    - แบรนด์นี้มีการทำงานร่วมกับนักกีฬาชั้นนำและศิลปินที่มีชื่อเสียงในการสร้างผลิตภัณฑ์ร่วมกัน.
    
    -การทำงานอย่างสร้างสรรค์:
    - ไนกี้มีการทำงานเป็นสร้างสรรค์ (innovative) ทั้งในด้านดีไซน์และเทคโนโลยีผลิตภัณฑ์.
    
    -ส่งเสริมกีฬาและกิจกรรมกีฬา:
    - Nike เป็นที่รู้จักในการสนับสนุนทีมกีฬา นักกีฬา, และกิจกรรมทางกีฬาทั่วๆ ไป.
    
    -ยังคงเป็นที่รู้จักทั่วโลก:
    - ไนกี้เป็นหนึ่งในแบรนด์ที่มีชื่อเสียงทั่วโลกและมีการตลาดทั้งในภูมิภาคและโลก.
    การบูรณะทั้งทางธุรกิจและการสร้างผลิตภัณฑ์ที่มีคุณภาพมีส่วนสำคัญในความเป็นที่รู้จักและความนิยมของแบรนด์ Nike.         
        """)


    

product_data = {
    'รายการสินค้า': [1, 2, 3, 4, 5, 6, 7, 8, 9 ,],
    'สินค้า': ['NIKE ZOOM MERCURIAL SUPERFLY ELITE 9 MDS IRON STUD FOOTBALL SHOES (SG) ANTI-CLOG BRIGHT RED ORANGE BLACK WHITE', 'NIKE PHANTOM ELITE GX IRON-NOP FOOTBALL SHOES (SG) ANTI-CLOG BRIGHT RED BLACK WHITE', 'NIKE PHANTOM GX II ELITE MAD READY IRON-NOP FOOTBALL SHOES (SG) ANTI-CLOG BLACK OFF-WHITE GOLD', 'NIKE ZOOM MERCURIAL SUPERFLY 9 ELITE IRON STUD FOOTBALL SHOES (SG) ANTI-CLOG OFF WHITE BLACK', 'NIKE TIEMPO LEGEND ACADEMY 10 IRON NOP FOOTBALL SHOES (SG) ANTI-CLOG TURQUOISE BLACK PURPLE WHITE', 'NIKE ZOOM MERCURIAL VAPOR 15 ELITE GRAS FOOTBALL SHOES (FG) BRIGHT GREEN BLACK GREEN', 'NIKE PHANTOM LUNA II SHADOW ELITE GRAS FOOTBALL SHOES (FG) BLACK DARK GREY', 'NIKE ZOOM MERCURIAL SUPERFLY 9 ELITE GRAS FOOTBALL SHOES (FG) BLACK BLUE WHITE', 'NIKE PHANTOM GX ACADEMY GRASS/ARTIFICIAL GRASS FOOTBALL SHOES (MG) ORANGE BLACK'],
    'ราคา': [11700, 10100, 10500, 11300, 3500, 10500, 10900, 10900, 3300],
    'รูปภาพ': ['https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/4/244171_nike-zoom-mercurial-superfly-9-elite-mds-ijzeren-nop-voetbalschoenen-sg-anti-cl_1.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/2/226437_nike-phantom-gx-elite-ijzeren-nop-voetbalschoenen-sg-anti-clog-zwart-felrood-wi.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/5/252534_nike-phantom-gx-ii-elite-ijzeren-nop-voetbalschoenen-sg-anti-clog-zwart-gebroke_1.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/5/252109_nike-zoom-mercurial-superfly-9-elite-ijzeren-nop-voetbalschoenen-sg-anti-clog-g.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/3/237893_nike-tiempo-legend-10-academy-ijzeren-nop-voetbalschoenen-sg-anti-clog-turquois.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/5/253765_nike-zoom-mercurial-vapor-15-elite-mds-gras-voetbalschoenen-fg-felgroen-zwart-g.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/5/250597_nike-phantom-luna-ii-elite-gras-voetbalschoenen-fg-zwart-donkergrijs.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/3/231249_nike-zoom-mercurial-superfly-9-elite-gras-voetbalschoenen-fg-zwart-blauw-wit.jpg', 'https://www.knvbshop.nl/media/catalog/product/cache/d81c8dc66c69ceb69419c2e7e72e896d/2/2/227941_nike-phantom-gx-academy-gras-kunstgras-voetbalschoenen-mg-oranje-zwart.jpg'],
    'ประเภท': ['A', 'B', 'A', 'C', 'B', 'C', 'A', 'B', 'C']  # เพิ่มประเภทสินค้า
}

df_products = pd.DataFrame(product_data)

# ระบบตะกร้า
class ShoppingCart:
    def __init__(self):
        self.cart = []

    def add_to_cart(self, product_id, quantity):
        product = df_products[df_products['รายการสินค้า'] == product_id].iloc[0]
        total_price = product['ราคา'] * quantity
        self.cart.append({'รายการสินค้า': product_id, 'สินค้า': product['สินค้า'],
                           'ปริมาณ': quantity, 'ราคารวม': total_price})

    def get_cart_total(self):
        return sum(item['ราคารวม'] for item in self.cart)

# สร้าง instance ของ ShoppingCart
shopping_cart = ShoppingCart()

color_code = "#E07A5F"  # รหัสสี HEX

title_html = f"""
    <style>
        .title-container {{
            background-color: {color_code};
            padding: 10px;
            text-align: center;
            width: %;  /* ปรับความกว้างตามที่คุณต้องการ */
            margin: auto;  /* จัดตำแหน่งกลางหน้าจอ */
        }}
        .title {{
            color: white;
        }}
    </style>
    <div class="title-container">
        <h1 class="title">FOCUSSPORT ⚽</h1>
    </div>
"""

st.markdown(title_html, unsafe_allow_html=True)

# Sidebar
selected_product_id_sidebar = st.sidebar.selectbox('เลือกสินค้า:', df_products['รายการสินค้า'])
selected_product_sidebar = df_products[df_products['รายการสินค้า'] == selected_product_id_sidebar].iloc[0]

# แสดงภาพสินค้าใน sidebar
st.sidebar.image(selected_product_sidebar['รูปภาพ'], caption=selected_product_sidebar['สินค้า'], use_column_width=True)

# Sidebar buttons
if st.sidebar.button('ราคาต่ำสุด-สูงสุด'):
    st.header('สินค้าทั้งหมด (ราคาต่ำสุด-สูงสุด)')
    all_products_sorted_by_price = df_products.sort_values(by='ราคา')
    st.dataframe(all_products_sorted_by_price)

if st.sidebar.button('ราคาสูงสุด-ต่ำสุด'):
    st.header('สินค้าทั้งหมด (ราคาสูงสุด-ต่ำสุด)')
    all_products_sorted_by_price_desc = df_products.sort_values(by='ราคา', ascending=False)
    st.dataframe(all_products_sorted_by_price_desc)


if st.sidebar.button('สินค้าใหม่'):
    st.header('สินค้าใหม่')
    new_products = df_products.sort_values(by='รายการสินค้า', ascending=False).head(3)
    st.dataframe(new_products)

# แสดงรายการสินค้าเป็นคอลัมน์
num_columns = 3
products_per_column = len(df_products) // num_columns
for i in range(0, len(df_products), products_per_column):
    cols = st.columns(num_columns)
    for j in range(num_columns):
        index = i + j
        if index < len(df_products):
            with cols[j]:
                st.image(df_products.iloc[index]['รูปภาพ'], use_column_width=True)
                st.write(f"**สินค้า:** {df_products.iloc[index]['สินค้า']}")
                st.write(f"**ราคา:** {df_products.iloc[index]['ราคา']:,.0f} บาท")
                button_key = f"select_product_{df_products.iloc[index]['รายการสินค้า']}"
                if st.button('เลือกสินค้า', key=button_key):
                    shopping_cart.add_to_cart(df_products.iloc[index]['รายการสินค้า'], 1)
                    st.success('เพิ่มสินค้าลงในตะกร้าเรียบร้อย')
                    
                    # Navigate to the next page (ราคาที่ต้องชำระ)
                    next_page_url = f"/selected_product/{df_products.iloc[index]['รายการสินค้า']}"
                    st.experimental_set_query_params(next_page=next_page_url)

# Display the shopping cart in the sidebar
st.sidebar.header("ตะกร้าสินค้า")
for item in shopping_cart.cart:
    st.sidebar.write(f"**{item['สินค้า']} x{item['ปริมาณ']}** - {item['ราคารวม']:,.0f} บาท")

# Add an "Order Now" button
if st.sidebar.button('สั่งซื้อสินค้า'):
    order_total = shopping_cart.get_cart_total()
    st.sidebar.success(f"คำสั่งซื้อของคุณสำเร็จแล้ว ")
    
# ฟังก์ชันการค้นหา
search_query = st.sidebar.text_input('ค้นหาสินค้า')
filtered_products = df_products[df_products['สินค้า'].str.contains(search_query, case=False)]

# ตรวจสอบว่ามีการค้นหาหรือไม่
if not filtered_products.empty:
    st.header('ผลลัพธ์การค้นหา:')
    st.dataframe(filtered_products)
else:
    st.warning('ไม่พบสินค้าที่ตรงกับคำค้นหา')



