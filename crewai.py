#pip install crewai

from crewai import Agent, Task, Crew

# Step 1: Define the agents

math_agent = Agent(
    role="Mathematician",
    goal="Solve simple math equations accurately",
    backstory="A skilled mathematician who specializes in basic arithmetic operations.",
    verbose=True
)

verifier_agent = Agent(
    role="Verifier",
    goal="Verify the correctness of math solutions",
    backstory="A diligent verifier who ensures that calculations are correct.",
    verbose=True
)

# Step 2: Define the tasks

math_task = Task(
    description="Solve the equation: 3 + 5",
    agent=math_agent
)

verification_task = Task(
    description="Verify if the result of 3 + 5 is correct",
    agent=verifier_agent
)

# Step 3: Create the CrewAI team

crew = Crew(
    agents=[math_agent, verifier_agent],
    tasks=[math_task, verification_task]
)

# Step 4: Execute the tasks

crew.kickoff()
