#program pro Arduino
void setup() //vykoná se při startu
{
    Serial.begin(9600); //kanál seriové komunikace
    pinMode(13, OUTPUT); //nastavení diody 13 na output
}

void loop()
{

    if (Serial.available())
    {
        switch (Serial.read())
        {
            case '1':     //když bude 1 dioda se rozvsítí
                digitalWrite(13, HIGH);
                break;
            default:
                digitalWrite(13, LOW);
                break;
        }
    }
}


# program na čtení dat z Arduina
void setup() {
  Serial.begin(9600);
}

void loop() {
    Serial.print("Hello World");
    delay(1000);
}
