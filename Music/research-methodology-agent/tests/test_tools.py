from tools import define_research_question, select_methodology, create_methodology_plan


def test_question_validation():
    assert not define_research_question.run({'topic':'x'}).ok


def test_method_selection_randomized():
    r=select_methodology.run({'objective':'estimate treatment effect','intervention':True,'randomization':True}); assert r.ok and r.data['candidates'][0]['method']=='randomized-controlled-trial'


def test_method_selection_qualitative():
    r=select_methodology.run({'objective':'understand experiences','qualitative':True}); assert r.ok and r.data['candidates'][0]['method']=='qualitative-study'


def test_plan():
    r=create_methodology_plan.run({'research_question':'Does training improve test performance?','method':'randomized-controlled-trial'}); assert r.ok and 'analysis' in r.data['plan']
