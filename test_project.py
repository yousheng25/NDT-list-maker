from project import mt_pt_machine, ut_rt_machine,remarks_machine,input_name

def main():
    test_mtpt()
    test_utrt()
    test_remarks()
    test_name()

def test_mtpt():
    assert mt_pt_machine("TI-6242","TI-6242","A","Full penetration weld")==("100%","168 hours","")
    assert mt_pt_machine("TI-6242","INCONEL 718","A","Full penetration weld")==("100%","168 hours","")
    assert mt_pt_machine("TI-6242","INCONEL 718","B","Full penetration weld")==("100%","24 hours","")
    assert mt_pt_machine("TI-6242","INCONEL 718","C","Full penetration weld")==("100%","Normal temperature","")
    assert mt_pt_machine("TI-6242","INCONEL 718","D","Full penetration weld")==("N/A","N/A","")

def test_utrt():
    assert ut_rt_machine("TI-6242","TI-6242","A","Full penetration weld")==("100%","48 hours","")
    assert ut_rt_machine("TI-6242","INCONEL 718","A","Full penetration weld")==("N/A","N/A","Replacing by MT/PT in each welding layer")
    assert ut_rt_machine("TI-6242","INCONEL 718","B","Full penetration weld")==("N/A","N/A","")
    assert ut_rt_machine("TI-6242","INCONEL 718","C","Full penetration weld")==("N/A","N/A","")
    assert ut_rt_machine("TI-6242","INCONEL 718","D","Full penetration weld")==("N/A","N/A","")
def test_remarks():
    assert remarks_machine("test01","test02")==("test01, test02")
    assert remarks_machine("","test02")==("test02")
    assert remarks_machine("test01","")==("test01")


if __name__ == "__main__":
    main()
