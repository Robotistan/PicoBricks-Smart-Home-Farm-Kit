#include <picobricks.h>

int doorClosed   = 80;
int windowClosed = 50;
motorDriver motor;

void setup() {
  // Close window and door initially
  motor.servo(4, doorClosed);
  motor.servo(2, windowClosed);
}

void loop() {
  
}
