## Projeto de Eventos

[![My Skills](https://skillicons.dev/icons?i=py,flask,sqlite)](https://skillicons.dev)

Projeto realizado por ocasião do evento < nlw /> unite da RocketSeat. 

A trilha é Python e o projeto é criado utilizando o framework Flask. 

Trata-se de um software de eventos presenciais, em que é possível:
  - Organizador pode:
      - Cadastrar eventos (com informações de título, detalhes, slogan e número máximo de participantes);
      - Obter informações de um evento;
      - Obter a lista de participantes de um evento.
  - Partipante pode:
      - Inscrever-se em um evento;
      - Obter o crachá de inscrição de um evento;
      - Realizar o check-in em eventos.

Os endpoints criados para cada umas ações acima são:
  - /events
  - /events/< event_id >
  - /events/< event_id >/attendees
  - /events/< event_id >/register
  - /attendees/< attendee_id >/badge
  - /attendees/< attendee_id >/check-in

As dependências utilizadas são:
  - Flask;
  - Flask CORS;
  - SQLAlquemy;
  - Pytest.

Dados são persistidos em um banco de dados relacional SQLite. O diagrama de dados é o seguinte:
![image](https://github.com/LuganThierry/nlw-unite/assets/106288264/760ed966-c223-4625-af89-899939d8d9a5)
