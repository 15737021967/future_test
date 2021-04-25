import click
import random

from ezreal import app, db
from ezreal.demo.models import DemoModel


@app.cli.command("create-demo-data")
@click.option('--count')
def create_demo_data(count: int):
    count = int(count)
    for item in range(count):
        ins_list = [
            DemoModel(name=f"test-{item}{i}", age=random.randint(0, 18), sex=random.randint(0, 1))
            for i in range(item)
        ]
        db.session.add_all(ins_list)
        db.session.commit()
