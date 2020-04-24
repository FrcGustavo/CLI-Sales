import click

from clients.services import ClientsService
from clients.models import ClientModel

@click.group()
def clients():
  """Manages the clients lifecycle"""
  pass


@clients.command()
@click.option('-n', '--name', type=str, prompt=True, help='The client name')
@click.option('-c', '--company', type=str, prompt=True, help='The client company')
@click.option('-e', '--email', type=str, prompt=True, help='The client email')
@click.option('-p', '--position', type=str, prompt=True, help='The client position')
@click.pass_context
def create(ctx, name, company, email, position):
  """Create a new client"""
  client = ClientModel(name, company, email, position)
  client_service = ClientsService(ctx.obj['clients_table'])
  client_service.create_client(client)


@clients.command()
@click.pass_context
def list(ctx):
  """List all clients"""
  client_service = ClientsService(ctx.obj['clients_table'])
  clients_list = client_service.list_clients()
  click.echo('|  ID  |  NAME  |  COMPANY  |  EMAIL  |  POSITION  |')
  click.echo('*'*100)
  for client in clients_list:
    click.echo('|  {}  |  {}  |  {}  |  {}  |  {}  |'.format(
      client['uid'],
      client['name'],
      client['company'],
      client['email'],
      client['position'],
    ))


@clients.command()
@click.pass_context
def update(ctx, client_uid):
  """Updates a client"""
  pass


@clients.command()
@click.pass_context
def delete(ctx, client_uid):
  """Deletes a clients"""
  pass


all = clients
