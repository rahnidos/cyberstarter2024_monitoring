# Sekurak Cyberstarter 2024
## Co w hostach piszczy, czyli jak ogarnąć monitoring infrastruktury i mieć czas na CS-a? :-)

Materiały do prelekcji w ramach wydarzenia: [https://sklep.securitum.pl/sekurak-cyberstarter](https://sklep.securitum.pl/sekurak-cyberstarter)
Prelekcja odbyła się 06.12.2024 12:00-13:00 w ścieżce Cyberstarter Admina

## Prezentacja
Export prezentacji do PDF: [CyberStarter - Co w hostach piszczy](./CyberStarter%20-%20Co%20w%20hostach%20piszczy.pdf)

## Pliki konfiguracyjne
[konfiguracja_nagios](./konfiguracja_nagios/)  
Pliki konfiguracyjne zrzucone z systemu zainstalowanego na potrzeby prezentacji. W większości są to oryginalne pliki Centreona, zamieszczam je do porównania w razie problemów. 

[konguracja_nsclient](./konfiguracja_nsclient/)  
Plik konfiguracyjny nsclient.ini na przykładowym hoście. W pliku znajduje się definicja, użytej podczas prezentacji, komendy check_em_file. 
**UWAGA!** Na potrzeby prezentacji w lokalnej sieci wirtualnej wyłączyłem szyfrowanie komunikacji między klientem a nagiosem:
```
use ssl = false
```
W prawdziwej konfiguracji zdecydowanie zalecam włączyć to szyfrowanie.  
Na uwagę zasługuje jeszcze linia: 
```
[/settings/external scripts]
allow arguments=true
```
Taka konfiguracja pozwala na przyjmowanie lokalnym skryptom argumentów. 

[konfiguracja_snmpd](./konfiguracja_snmpd/)  
Przykładowy plik konfiguracyjny agenta SNMP. Jest to wstępna konfiguracja dla wersji 2c i community *cyberstarter*.
Konfigurację w produktywnym systemie warto oprzeć o polityki i zasady bezpieczeństwa funkcjonujące w organizacji.

## Screenshoty z Centreona
[konifguracja_centreon](./konfiguracja_centreon/)  
W tym katalogu znajdziecie screenshoty z centreona z konfiguracją omawianych podczas prezentacji rzeczy.

## Skrypty
[check_lastupdate.py](./skrypty/check_lastupdate.py)   
Skrypt do przykładu monitorowania wartości w bazie danych. W tym konkretnym przypadku plik sprawdza jak dawno temu miał miejsce ostatni insert do tabeli. Informacja o czasie insertu jest przechowywana w kolumnie *datein*.  
Skrypt przyjmuje jako parametr hasło do bazy dla użytkownika centreon. Warto zwrócić uwagę na obcięcie takiemu użytkownikowi uprawnień do niezbędnego minimum. Hasło w tym wypadku jest przechowywane w konfiguracji Centreona. W pełnej implementacji rozwiązania można pomyśleć o menadżerze haseł na serwerze centreona.  
Skrypt zwraca:
- System exit 0 - dla stanu OK, kiedy od ostatniego insertu upłynęło mniej niż 15 minut.
- System exit 1 - dla stanu WARN, ostatni insert więcej niż 15 minut, ale mniej niż 30.
- System exit 2 - dla stanu CRITICAL, ostatni insert więcej niż 30 minut temu.
- System exit 3 - dla stanu UNKNOWN, w przypadku probemów połączenia z bazą danych, lub pobraniem z niej informacji. 
  
[check_em_file.ps1](./skrypty/check_em_file.ps1)  
Skrypt użyty w przykładzie o sprawdzaniu pliku z awaryjnym zrzutem z bazy danych.  
Jako argumenty skrypt przyjmuje:
-  akceptowalną liczbę dni 
-  akceptowalną wielkość pliku
-  nazwę pliku (opcjonalnie)

Skrypt zwraca:
- System exit 0 (OK)- dla pliku młodszego niż liczba dni i większego niż akceptowalna wielkość.
- System exit 1 (WARN)- dla pliku młodszego, ale mniejszego niż akceptowalna wielkość.
- System exit 2 (CRITICAL) - w przypadku kiedy pliku nie ma lub nie spełnia powyższych warunków. 

## Linki
- [Centron Open Source](https://www.centreon.com/centreon-editions/centreon-open-source/)  
- [NSClient++](https://nsclient.org/)  
- [Nagios](https://www.nagios.org/)  
- [Nagios NRPE](https://exchange.nagios.org/directory/Addons/Monitoring-Agents/NRPE--2D-Nagios-Remote-Plugin-Executor/details)  





