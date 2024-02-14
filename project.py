import csv

def main():
    ndt_list=str(input_name())
    with open(ndt_list, newline='') as csvfile:
        # 讀取 CSV 檔內容，將每一列轉成一個 dictionary
        reader = csv.reader(csvfile)
        title= next(reader)[1] #讀取文件下一行
        date = next(reader)[1] #讀取文件下一行
        print(f"Title : {title}")
        print(f"Date : {date}")
        output_name="NDT_Requirements-" + title + " output" + ".csv"
        print(output_name)
        data = csv.DictReader(csvfile)

        # Writting output
        with open(output_name, 'w', newline='') as csvfile:
            # 以","分隔欄位，建立 CSV 檔寫入器
            writer = csv.writer(csvfile, delimiter=',')
            writer.writerow(['System name', title])
            writer.writerow(['Date', date])
            writer.writerow(['Part number', 'Material of Base', 'Material of Parts', 'Structure Category', 'Welding Category', 'Drawing', 'MT/PT Minimum Required Efficiency', 'MT/PT Final Inspection time', 'UT/RT Minimum Required Efficiency', 'UT/RT Final Inspection time', 'Remarks'])

            # looping into each dictionary
            for row in data:
            # reading in specific format
                row["Part number"]=str(row["Part number"]).upper()
                row["Material of Base"]=str(row["Material of Base"]).upper()
                row["Material of Parts"]=str(row["Material of Parts"]).upper()
                row["Structure Category"]=str(row["Structure Category"]).upper()
                row["Welding Category"]=str(row["Welding Category"]).capitalize()
            # MT & PT Logic decision
                row["MT/PT Minimum Required Efficiency"]=mt_pt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[0]
                row["MT/PT Final Inspection time"]=mt_pt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[1]

                mt_pt_remarks=mt_pt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[2]

            # UT & RT Logic decision
                row["UT/RT Minimum Required Efficiency"]=ut_rt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[0]
                row["UT/RT Final Inspection time"]=ut_rt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[1]
                ut_rt_remarks=ut_rt_machine(row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"])[2]

            # Total Logic decision
                row["Remarks"]=remarks_machine(mt_pt_remarks,ut_rt_remarks)
                print (row["Part number"],row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"],row["MT/PT Minimum Required Efficiency"], row["MT/PT Final Inspection time"],row["UT/RT Minimum Required Efficiency"], row["UT/RT Final Inspection time"],row["Remarks"])
                writer.writerow([row["Part number"],row["Material of Base"],row["Material of Parts"],row["Structure Category"],row["Welding Category"],row["MT/PT Minimum Required Efficiency"], row["MT/PT Final Inspection time"],row["UT/RT Minimum Required Efficiency"], row["UT/RT Final Inspection time"],row["Remarks"]])




def mt_pt_machine(m_base,m_part,s_category,w_category):
    if s_category=="A" and w_category in("Butt weld", "Full penetration weld", "Partial penetration weld"):
        if m_base==m_part:
            efficiency="100%"
            inspection_time="168 hours"
            remarks=""
            return efficiency,inspection_time,remarks
        else:
            efficiency="100%"
            inspection_time="168 hours"
            remarks=""
            return efficiency,inspection_time,remarks

    elif s_category=="A" and w_category=="Fillet weld":
        efficiency="100%"
        inspection_time="72 hours"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="B" and w_category in ("Butt weld", "Full penetration weld", "Partial penetration weld", "Fillet weld"):
        efficiency="100%"
        inspection_time="24 hours"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="C" and w_category in ("Full penetration weld", "Partial penetration weld", "Fillet weld"):
        efficiency="100%"
        inspection_time="Normal temperature"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="D" and w_category in ("Full penetration weld", "Partial penetration weld", "Fillet weld"):
        efficiency="N/A"
        inspection_time="N/A"
        remarks=""
        return efficiency,inspection_time,remarks
    else:
        efficiency="ERROR INPUT"
        inspection_time="ERROR INPUT"
        remarks=""
        return efficiency,inspection_time,remarks

def ut_rt_machine(m_base,m_part,s_category,w_category):
    if s_category=="A" and w_category in("Butt weld", "Full penetration weld", "Partial penetration weld"):
        if m_base==m_part:
            efficiency="100%"
            inspection_time="48 hours"
            remarks=""
            return efficiency,inspection_time,remarks
        else:
            efficiency="N/A"
            inspection_time="N/A"
            remarks="Replacing by MT/PT in each welding layer"
            return efficiency,inspection_time,remarks
            #remarks 回傳 新增欄位

    elif s_category=="A" and w_category=="Fillet weld":
        efficiency="100"
        inspection_time="12 hours"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="B" and w_category=="Butt weld":
        efficiency="100%"
        inspection_time="12 hours"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="B" and w_category in ("Full penetration weld", "Partial penetration weld","Fillet weld"):
        efficiency="N/A"
        inspection_time="N/A"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="C" and w_category in ("Full penetration weld", "Partial penetration weld","Fillet weld"):
        efficiency="N/A"
        inspection_time="N/A"
        remarks=""
        return efficiency,inspection_time,remarks

    elif s_category=="D" and w_category in ("Full penetration weld", "Partial penetration weld","Fillet weld"):
        efficiency="N/A"
        inspection_time="N/A"
        remarks=""
        return efficiency,inspection_time,remarks

    else :
        efficiency="ERROR INPUT"
        inspection_time="ERROR INPUT"
        remarks=""
        return efficiency,inspection_time,remarks

def remarks_machine(front, after):
    if front!="" and after!="":
        return str(front +", "+ after)
    elif front!="" and after=="":
        return str(front)
    else:
        return str(after)

def input_name():

    while True:
        name = input("input the name of NDT list: ")
        if name.endswith('.csv'):
            try:
                with open(name, newline='') as csvfile:
                    pass
            except FileNotFoundError:
                print('Error input,this file is not in the folder.')
                continue
            break
        else:
            print('Error input, not csv file, please try again.')
    return name

if __name__ == "__main__":
    main()
