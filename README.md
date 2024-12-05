# Sekurak Cyberstarter 2024
## Co w hostach piszczy, czyli jak ogarnąć monitoring infrastruktury i mieć czas na CS-a? :-)

Materiały do prelekcji w ramach wydarzenia: [https://sklep.securitum.pl/sekurak-cyberstarter](https://sklep.securitum.pl/sekurak-cyberstarter)
Prelekcja odbyła się 06.12.2024 12:00-13:00 w ścieżce Cyberstarter Admina

## Prezentacja
Export prezentacji do PDF: [CyberStarter - Co w hostach piszczy](./CyberStarter%20-%20Co%20w%20hostach%20piszczy.pdf)

## Pliki konfiguracyjne

## Screenshoty z Centreona

## Skrypty
[check_lastupdate.py](./skrypty/check_lastupdate.py)
Skrypt do przykładu monitorowania wartości w bazie danych. W tym konkretnym przypadku plik sprawdza jak dawno temu miał miejsce ostatni insert do tabeli. Informacja o czasie insertu jest przechowywana w kolumnie *datein*. 
Skrypt przyjmuje jako parametr hasło do bazy dla użytkownika centreon. Warto zwrócić uwagę na obcięcie takiemu użytkownikowi uprawnień do niezbędnego minimum. Hasło w tym wypadku jest przechowywane w konfiguracji Centreona. W pełnej implementacji rozwiązania można pomyśleć o menadżerze haseł na serwerze centreona. 
Skrypt zwraca:
    - System exit 0 - dla stanu OK, kiedy od ostatniego insertu upłynęło mniej niż 15 minut.
    - System exit 1 - dla stanu WARN, ostatni insert więcej niż 15 minut, ale mniej niż 30.
    - System exit 2 - dla stanu CRITICAL, ostatni insert więcej niż 30 minut temu.
    - System exit 3 - dla stanu UNKNOWN, w przypadku probemów połączenia z bazą danych, lub pobraniem z niej informacji. 
  




