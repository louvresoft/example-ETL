from prefect import task, Flow


@task
def load():
    print("Hola mundo")


with Flow("p1.1 - Hello world") as flow:
    load()

# Ejecutamos un flow
flow.run()
