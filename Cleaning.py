import pandas as pd
import numpy as np

pd.set_option("display.max_rows", None)  # แสดงทุกแถว
pd.set_option("display.max_columns", None)  # แสดงทุกคอลัมน์

filename = "/Users/gene/Downloads/MIS/Takehome_data.xlsx"
df = pd.read_excel(filename)
col_name = df.columns

# write all columns to text file
with open("col.txt", "wt", encoding="utf-8") as f:
    f.write("\n".join([c for c in col_name]))

# Drop some columns that not use to analyse
d_columns = ["Timestamp", "ภาควิชา/ฝ่าย/ศูนย์/สถานี"]
df = df[df.columns[:35]]
df = df.drop(columns=d_columns)

# drop duplicated data
df = df.drop_duplicates()

# drop false information ข้อมูลบอกว่าเคยใช้แต่่ไม่มีคะแนน
df = df.drop(index=31)


# Rename Columns
r_columns = {
    "วิทยาเขต": "Campus",
    "คณะ/สถาบัน/สำนัก": "Faculty",
    "อายุงานที่มหาวิทยาลัยเกษตรศาสตร์": "Experience",
    "คุณเคยใช้บริการระบบสารสนเทศงานวิจัย KUR, KUR3, KURX หรือ KUForest หรือไม่": "Information_sys",
    "1. ระบบสารสนเทศ online (e.g. KUR, KUR3, KURX, Tracking, KU Forest) จากหน้า website หลัก [การแสดงผล สี กราฟิก สวยงาม อ่านง่าย]": "Inform_disp",
    "1. ระบบสารสนเทศ online (e.g. KUR, KUR3, KURX, Tracking, KU Forest) จากหน้า website หลัก [การจัดระบบเนื้อหา และ การเข้าถึงข้อมูล (การจัดเมนู สัญลักษณ์ ไอคอน การสื่อความหมาย ตำแหน่ง ลิงค์ต่างๆ)]": "Inform_pos",
    "1. ระบบสารสนเทศ online (e.g. KUR, KUR3, KURX, Tracking, KU Forest) จากหน้า website หลัก [ความมั่นคงปลอดภัยของระบบสารสนเทศและฐานข้อมูลงานวิจัย ]": "Inform_secure",
    "1. ระบบสารสนเทศ online (e.g. KUR, KUR3, KURX, Tracking, KU Forest) จากหน้า website หลัก [ข้อมูลงานวิจัยสามารถนำไปใช้ประโยชน์ด้านต่างๆ ได้]": "inform_bene",
    "1. ระบบสารสนเทศ online (e.g. KUR, KUR3, KURX, Tracking, KU Forest) จากหน้า website หลัก [ความพึงพอใจของภาพรวมต่อระบบสารสนเทศงานวิจัย]": "Inform_sasti",
    "2. ท่านเคยใช้ระบบ KUR3 หรือไม่": "KUR3",
    "2.1 KUR3: ระบบงานวิจัยและงานสร้างสรรค์ [ความเข้าใจง่าย/สื่อความหมาย และ ครบถ้วนของ tab รายการ]": "KUR3_userfriendly_tab",
    "2.1 KUR3: ระบบงานวิจัยและงานสร้างสรรค์ [ความใช้ง่ายของระบบ KUR3 ในการตรวจสอบและแก้ไขข้อมูล ]": "KUR3_userfriendly_sys",
    "2.1 KUR3: ระบบงานวิจัยและงานสร้างสรรค์ [ระบบ KUR3 ครอบคลุมผลงานวิจัยของท่าน และ มีความถูกต้อง]": "KUR3_correct",
    "2.2 ปัญหาที่พบ หรือ ข้อเสนอแนะอื่นๆ ของระบบ KUR3": "KUR3_suggest",
    "3. คุณเคยใช้ระบบ KUR หรือไม่": "KUR",
    "3.1 KUR: ระบบบริหารจัดการโครงการวิจัย [ความเข้าใจง่าย/สื่อความหมาย และ ครบถ้วนของ tab รายการ]": "KUR_userfriendly_tab",
    "3.1 KUR: ระบบบริหารจัดการโครงการวิจัย [ความใช้ง่ายของระบบ KUR ]": "KUR_userfriendly_sys",
    "3.1 KUR: ระบบบริหารจัดการโครงการวิจัย [ความถูกต้องของข้อมูลในระบบ KUR]": "KUR_correct",
    "3.2 ปัญหาที่พบ หรือ ข้อเสนอแนะอื่นๆ ของระบบ KUR": "KUR_suggest",
    "4. คุณเคยใช้ระบบ KURX หรือไม่": "KURX",
    "4.1 KURX: ระบบบริหารเงินอุดหนุนวิจัย [ความเข้าใจง่าย/สื่อความหมาย และ ครบถ้วนของ tab รายการ]": "KURX_userfriendly_tab",
    "4.1 KURX: ระบบบริหารเงินอุดหนุนวิจัย [ความใช้ง่ายของระบบ KURX ในการเบิกจ่าย]": "KURX_userfriendly_sys",
    "4.1 KURX: ระบบบริหารเงินอุดหนุนวิจัย [ความถูกต้องในการโอนเงินของระบบ KURX]": "KURX_correct",
    "4.2 ปัญหาที่พบ หรือ ข้อเสนอแนะอื่นๆ ของระบบ KURX": "KURX_suggest",
    "5. คุณเคยใช้ระบบ KUForest หรือไม่": "KUForest",
    "5.1 KUForest: ระบบสืบค้นข้อมูลงานวิจัย [ความใช้ง่ายของระบบ KUForest ]": "KUForest_userfriendly_sys",
    "5.1 KUForest: ระบบสืบค้นข้อมูลงานวิจัย [ความถูกต้อง ครบถ้วนของข้อมูล]": "KUForest_correct",
    "6. ความพึงพอใจต่อการให้บริการของเจ้าหน้าที่ [เจ้าหน้าที่ให้คำแนะนำหรือตอบข้อซักถามได้อย่างดี]": "staff_sasti",
    "6. ความพึงพอใจต่อการให้บริการของเจ้าหน้าที่ [เจ้าหน้าที่ให้บริการด้วยความสุภาพ เอาใจใส่ และ กระตือรือร้น]": "staff_servicemind",
    "6. ความพึงพอใจต่อการให้บริการของเจ้าหน้าที่ [การเข้าถึง สามารถติดต่อเจ้าหน้าที่ได้ง่าย หลายช่องทาง]": "staff_contact",
    "6. ความพึงพอใจต่อการให้บริการของเจ้าหน้าที่ [เจ้าหน้าที่ช่วยแก้ไขปัญหาให้กับท่านได้ดี]": "staff_problemsolve",
    "6. ความพึงพอใจต่อการให้บริการของเจ้าหน้าที่ [เจ้าหน้าให้ข้อมูลที่ถูกต้อง น่าเชื่อถือ]": "staff_correct",
    "7. ปัญหา หรือ ข้อเสนอแนะอื่นๆ ในการปรับปรุงหน้า website ระบบสารสนเทศ": "Inform_suggest",
}
df = df.rename(columns=r_columns)


# Revalue Campus columns
campus_replacements = {
    "บางเขน": "Bangkhen",
    "บสงเขน": "Bangkhen",
    "กำแพงแสน": "KamphaengSaen",
    "ศรีราชา": "Sriracha",
    "เฉลิมพระเกียรติ จังหวัดสกลนคร": "SakonNakon",
    "วิทยาเขตเฉลิมพระเกียรติ จังหวัดสกลนคร": "SakonNakon",
}
df["Campus"] = df["Campus"].replace(campus_replacements)

# Revalue Faculty Columns
faculty_replacement = {
    "Agro Industry": "Agro_industry",
    "คณะทรัพยากรธรรมชาติและอุตสาหกรรมเกษตร": "Agro_industry",
    "ทรัพยากรธรรมชาติและอุตสาหกรรมเกษตร": "Agro_industry",
    "อุตสาหกรรมเกษตร": "Agro_industry",
    "คณะอุตสาหกรรมเกษตร": "Agro_industry",
    "Architecture": "Architecture",
    "เกษตร": "Agriculture",
    "เกษตร กำแพงแสน": "Agriculture",
    "คณะเกษตร": "Agriculture",
    "คณะเกษตร ": "Agriculture",
    "คณะเกษตร กำแพงแสน": "Agriculture",
    "คณะเกษตร กำแพงแสน ": "Agriculture",
    "คณะประมง": "Fisheries",
    "ประมง": "Fisheries",
    "คณะแพทยศาสตร์": "Medicine",
    "คณะมนุษยศาสตร์": "Humanities",
    "มนุษยศาสตร์": "Humanities",
    "คณะวิทยาการจัดการ": "Management Sciences",
    "คณะวิทยาศาสตร์": "Science",
    "วิทยาศาสตร์": "Science",
    "คณะวิศวกรรมศาสตร์": "Engineering",
    "คณะวิศวกรรมศาสตร์กำแพงแสน": "Engineering",
    "วิศว ฯ ศรช": "Engineering",
    "วิศวกรรมศาสตร์": "Engineering",
    "วิศวกรรมศาสตร์ ศรีราชา": "Engineering",
    "วิศวกรรมศาสตร์กำแพงแสน": "Engineering",
    "วิศวกรรมีศาสตร์ศรีราชา": "Engineering",
    "วิสวกรรมศาสตร์": "Engineering",
    "วิทยาศาสตร์และวิศวกรรมศาสตร์": "Science_and_Engineering",
    "ศิลปศาสตร์และวิทยาศาสตร์": "LiberalArts_and_Science",
    "คณะศึกษาศาสตร์": "Education",
    "ศึกษาศาสตร์": "Education",
    "ศึกษาศาสตร์และพัฒนศาสตร์": "Education_and_Development_Sciences",
    "คณะสังคมศาสตร์": "Social_Sciences",
    "สังคมศาสตร์": "Social_Sciences",
    "สัตวแพทยศาสตร์": "Veterinary_Medicine",
    "เทคนิคการสัตวแพทย์": "Veterinary_Technology",
    "วนศาสตร์": "Forestry",
    "วิทยาลัยบูรณาการศาสตร์": "Integrated_Science",
    "ศูนย์วิทยาศาสตร์ข้าว": "Rice_Science_Center",
    "สถาบันค้นคว้าและพัฒนาผลิตผลทางการเกษตรและอุตสาหกรรมเกษตร": "KAPI",
    "สถาบันค้นคว้าและพัฒนาผลิตภัณฑ์อาหาร": "IFRPD",
    "สถาบันวิจัยและพัฒนาแห่ง มหาวิทยาลัยเกษตรศาสตร์": "Research_and_Development_Institute",
}

df["Faculty"] = df["Faculty"].replace(faculty_replacement)

#Fill na with 0:
df= df.fillna(0)

# Revalue Information_sys ไม่เคยใช้ = 0 เคยใช้ = 1:
Information_sys_replacement = {"ไม่เคยใช้": 0, "เคยใช้": 1}
df["Information_sys"] = df["Information_sys"].replace(Information_sys_replacement)

# Revalue KUR3/KUR
KUR3_replacement = {"ไม่เคยใช้ (ข้ามไปทำข้อ 3.)": 0, "เคยใช้": 1}
KUR_replacement = {"ไม่เคยใช้ (ข้ามไปทำข้อ 4)": 0, "เคยใช้": 1}
KURX_replacement = {"ไม่เคยใช้": 0, "เคยใช้": 1}
KUForest_replacement = {"ไม่เคยใช้ (ข้ามไปทำข้อ 6.)": 0, "เคยใช้": 1}
df["KUR3"] = df["KUR3"].replace(KUR3_replacement)
df["KUR"] = df["KUR"].replace(KUR_replacement)
df["KURX"] = df["KURX"].replace(KURX_replacement)
df["KUForest"] = df["KUForest"].replace(KUForest_replacement)

# | Normalization Scoring:
columns_to_scale = [
    "Inform_disp",
    "Inform_pos",
    "Inform_secure",
    "inform_bene",
    "Inform_sasti",
    "KUR3_userfriendly_tab",
    "KUR3_userfriendly_sys",
    "KUR3_correct",
    "KUR_userfriendly_tab",
    "KUR_userfriendly_sys",
    "KUR_correct",
    "KURX_userfriendly_tab",
    "KURX_userfriendly_sys",
    "KURX_correct",
    "KUForest_userfriendly_sys",
    "KUForest_correct",
    "staff_sasti",
    "staff_servicemind",
    "staff_contact",
    "staff_problemsolve",
    "staff_correct",
]
# df[columns_to_scale] = df[columns_to_scale].apply(
#     lambda x: (x / 5)
# )  # 5 is a maximum score

# df[columns_to_scale] = scaler.fit_transform(df[columns_to_scale])
# df[columns_to_scale] = df[columns_to_scale].round(2)

df.to_excel("Processed_databaseMISTH.xlsx", index=False)

# define df1 for contain only quantity data
df1 = df.drop(columns=["KUR3_suggest", "KUR_suggest", "KURX_suggest", "Inform_suggest"])

df1.to_excel("df1.xlsx", index=False)
df1.to_csv("df1.csv",index=False)
# define df2 for contain only quality data
df2 = df[
    [
        "Campus",
        "Faculty",
        "Experience",
        "KUR3_suggest",
        "KUR_suggest",
        "KURX_suggest",
        "Inform_suggest",
    ]
]
df2.to_excel("df2.xlsx", index=False)
df2.to_csv("df2.csv",index=False)

