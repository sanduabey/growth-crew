import os
from crewai import Agent, Task, Process, Crew

#Load GPT-4
api_key = os.environ.get("OPENAI_API_KEY")

# print(api_key)

researcher = Agent(
  role="Market Researcher",
  goal="Research about the outsourcing industry and specifically outsourcing staff and business processes to Sri Lanka, the cost advantages it brings compared to labour expensive countries such as Australia. Find out how to find contact details, email addresses or phone numbers of business owners who might be interested in staff outsourcing services",
  backstory="You are an expert at gathering information, understanding the market demaind, target audience, and competition. You are great at finding potential clients from the Internet for my business - HR outsourcing to Sri Lanka.",
  verbose=True,
  allow_delegation=False
)

technologist = Agent(
  role="Technology expert",
  goal="Make assessment of how technologically feasible the company is and what type of technologies the company needs to adopt in order to succeed",
  backstory="You are a visionary in the thchnolgy realm, with a deep understanding of both current and emerging technological trends. Your expertiese lies not just in knowing the technology buy in foreseeing how it can be leveraged to solve real-world business problems and drive business innovation. You have a knack for identifying which technological solutions best fit different business models and needs, ensuring that our company stays ahead of the curve, offering best solutions to the customers. Your insights are crucial in aligning technology with business strategies, ensuring that the technological adoption not only enhances operational efficiency buy also provides a competitive edge in the marketplace",
  verbose=True,
  allow_delegation=True,
)

growth_consultant = Agent(
  role="Sales and Growth Expert",
  goal="As a Sales and Growth Specialist in a staff outsourcing business, the primary goal is to increase revenue by 25% within the next six months by securing 20 new clients from high-potential industries such as IT, healthcare, and finance, while enhancing customer retention by 20% through a robust client success program. This involves targeted marketing campaigns, upselling additional services to existing clients, expanding into new geographic markets, and implementing competitive analysis and innovative service offerings to achieve an increase of 15% market penetration. Additionally, the specialist should focus on improving the sales team's performance by 20% through regular training and mentorship, with key performance indicators including new client acquisition, quarterly and annual revenue growth, customer retention rates, market penetration, sales conversion rate improvement, and client satisfaction scores.",
  backstory="You are an expert Sales and Growth Specialist with over 15 years of experience in the staff outsourcing industry. Alex began their career as a junior sales representative at a small staffing agency, where their knack for understanding client needs and developing tailored solutions quickly set them apart. Over the years, Alex honed their skills in client acquisition, strategic market penetration, and revenue growth, consistently exceeding targets and driving company success. With a deep understanding of various high-potential industries, including IT, healthcare, and finance, Alex has a proven track record of expanding client bases and improving customer retention through innovative approaches and data-driven strategies. Known for their ability to lead and mentor sales teams, Alex has also significantly improved team performance and sales conversion rates through regular training and development programs. Now, as a seasoned professional, Alex leverages their extensive knowledge and experience to help businesses achieve sustainable growth and maintain a competitive edge in the dynamic staffing market.",
  verbose=True,
  allow_delegation=True,
)

task1 = Task(
  description="Gather a list of potential B2B customers that might be interested in outsourcing staffing and business processes to Sri Lanka with contact information",
  agent=researcher,
  expected_output="list of 100 names and contact details of suitable prospects"
)

task2 = Task(
  description="Identify best approach to communicate to the customers with intent of converting them into our customers",
  agent=technologist,
  expected_output="a bulletpoint step by step plan on how to customer outreach"
)

task3 = Task(
  description="Write a sequence of outreach emails and phone calls to reach out to the list of potential customers",
  agent=growth_consultant,
  expected_output="a sequence of highly effective sales pitches that can be sent via emails or text message or voice call script"
)

crew = Crew(
  agents=[researcher,technologist,growth_consultant],
  tasks=[task1, task2, task3],
  verbose=2,
  process=Process.sequential
)

result = crew.kickoff()

print("######################")
print(result)