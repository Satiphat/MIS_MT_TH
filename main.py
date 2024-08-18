import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_name = "df1.csv"
df1 = pd.read_csv(file_name)

# | Find_Key
campus_unqiue = df1["Campus"].unique()  # Find_Key
campus_faculty = df1["Faculty"].unique()
print("campus_unqiue:", campus_unqiue)
print("facuity_unique:", campus_faculty)


# | Count Stat
campus_count = pd.DataFrame(
    zip(campus_unqiue, [len(df1[df1.Campus == c]) for c in campus_unqiue])
)

facuity_count = pd.DataFrame(
    zip(campus_faculty, [len(df1[df1.Faculty == d]) for d in campus_faculty])
)

print(facuity_count)
# fig, ax = plt.subplots()
# ax.set_title("Campus")
# ax.pie(campus_count[1], labels=campus_count[0], autopct="%1.2f%%")
# plt.show()

df_inform = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "Information_sys",
        "Inform_disp",
        "Inform_pos",
        "Inform_secure",
        "inform_bene",
        "Inform_sasti",
    ]
]

df_inform = df_inform[df_inform["Information_sys"] != 0]
df_inform.to_excel("df_inform.xlsx", index=False)

df_KUR3 = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "KUR3",
        "KUR3_userfriendly_tab",
        "KUR3_userfriendly_sys",
        "KUR3_correct",
    ]
]
df_KUR3 = df_KUR3[df_KUR3["KUR3"] != 0]
df_KUR3.to_excel("df_KUR3.xlsx", index=False)

df_KUR = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "KUR",
        "KUR_userfriendly_tab",
        "KUR_userfriendly_sys",
        "KUR_correct",
    ]
]

df_KUR = df_KUR[df_KUR["KUR"] != 0]
df_KUR.to_excel("df_KUR.xlsx", index=False)


df_KURX = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "KURX",
        "KURX_userfriendly_tab",
        "KURX_userfriendly_sys",
        "KURX_correct",
    ]
]

df_KURX = df_KURX[df_KURX["KURX"] != 0]
df_KURX.to_excel("df_KURX.xlsx", index=False)

df_KUForest = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "KUForest",
        "KUForest_userfriendly_sys",
        "KUForest_correct",
    ]
]

df_KUForest = df_KUForest[df_KUForest["KUForest"] != 0]
df_KUForest.to_excel("df_KUForest.xlsx", index=False)

df_staff = df1[
    [
        "Campus",
        "Faculty",
        "Experience",
        "Information_sys",
        "staff_sasti",
        "staff_servicemind",
        "staff_contact",
        "staff_problemsolve",
        "staff_correct",
    ]
]

df_staff = df_staff[df_staff["Information_sys"] != 0]
df_staff.to_excel("df_staff.xlsx", index=False)
