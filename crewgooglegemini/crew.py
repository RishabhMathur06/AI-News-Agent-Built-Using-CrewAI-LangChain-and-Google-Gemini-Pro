from crewai import Crew, Process
from agents import news_researcher, news_writer
from tasks import research_task, write_task

# forming a tech-focused crew with advacned configurations
crew = Crew(
    agents=[news_researcher, news_writer],
    tasks=[research_task, write_task],
    process=Process.sequential,
)

# Starting the task exec process with enhanced feedback.
result = crew.kickoff(inputs={'topic':'AI in healthcare'})
print(result)
