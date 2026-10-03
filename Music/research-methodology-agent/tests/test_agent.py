from core.agent_core import AgentCore
from tools import define_research_question, select_methodology, create_methodology_plan


def core():
    c=AgentCore(); c.register(define_research_question); c.register(select_methodology); c.register(create_methodology_plan); return c


def test_discovery_and_question():
    c=core(); assert c.discover()==['create-methodology-plan','define-research-question','select-methodology']
    r=c.execute('define-research-question', {'topic':'sleep','population':'college students','outcome':'sleep quality'}); assert r.ok and 'college students' in r.data['question']


def test_unknown_tool():
    assert not core().execute('missing', {}).ok
