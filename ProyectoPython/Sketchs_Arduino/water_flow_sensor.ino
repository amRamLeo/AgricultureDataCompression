volatile int flow_frequency; // Measures flow sensor pulses
unsigned int l_hour; // Calculated litres/hour
unsigned char flowsensor = 2; // Sensor Input
unsigned long currentTime;
unsigned long cloopTime;
unsigned long previousSendTime = 0;  // Variable para realizar un seguimiento del tiempo de envío
const unsigned long sendInterval = 60000;  // Intervalo de 60 segundos

void flow () // Interrupt function
{
   flow_frequency++;
}

void setup()
{
   pinMode(flowsensor, INPUT);
   digitalWrite(flowsensor, HIGH); // Optional Internal Pull-Up
   Serial.begin(9600);
   attachInterrupt(0, flow, RISING); // Setup Interrupt
   sei(); // Enable interrupts
   currentTime = millis();
   cloopTime = currentTime;
}

void loop ()
{
   currentTime = millis();
   // Every second, calculate and print litres/hour data
   if(currentTime >= (cloopTime + 1000))
   {
      cloopTime = currentTime; // Updates cloopTime
      // Pulse frequency (Hz) = 7.5Q, Q is flow rate in L/min.
      l_hour = (flow_frequency * 60 / 7.5); // (Pulse frequency x 60 min) / 7.5Q = flowrate in L/hour
      flow_frequency = 0; // Reset Counter
   }

   // Send data only once every 5 seconds
   if (currentTime - previousSendTime >= sendInterval)
   {
      previousSendTime = currentTime;
      Serial.print(l_hour, DEC); // Print litres/hour
      Serial.println(); // Newline to indicate end of data
   }
}
