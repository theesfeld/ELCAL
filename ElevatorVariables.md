# Elevator Calculation Variable List

## Table Of Variables

|variable    |definition                                                    |
|------------|--------------------------------------------------------------|
|a           |acceleration (m/s2)                                           |
|CC          |car (rated) capacity (persons)                                |
|CF          |capacity factor (%)                                           |
|df          |average inter-floor height (m)                                |
|dfn         |height floor n (m)                                            |
|dH          |distance to reach reversal floor H excluding express zone (m) |
|dX          |total height of unserved floors in express zone (m)           |
|H           |average highest reversal floor                                |
|j           |jerk (m/s3)                                                   |
|L           |number of lifts                                               |
|N           |number of floors above main terminal                          |
|S           |average number of stops                                       |
|T           |cycle time (s)                                                |
|ta          |advanced door opening time (s)                                |
|tc          |door closing time (s)                                         |
|tfd(d)      |flight time flor travel distance d (s)                        |
|tfl         |single floor flight time (s)                                  |
|tl          |passenger loading time per person (s)                         |
|t0          |door opening time (s)                                         |
|tp          |average passenger transfer time (s)                           |
|tu          |passenger unloading time per person (s)                       |
|tv          |time to travel between two adjacent floors at rated speed (s) |
|ts          |time consumed when making a stop (s)                          |
|tstart      |allowance for motor start delay (s)                           |
|P           |average number of passengers in car                           |
|%POP        |5 minute up peak handling capacity (% population)             |
|RTT         |round trip time (s)                                           |
|Ueff        |effective building population (persons)                       |
|Ui          |population of floor i (persons)                               |
|UPPHC       |up peak handling capacity (persons/5min)                      |
|UPPINT      |average up peak interval (s)                                  |
|v           |contract (rated) speed (m/s)                                  |

## VARIABLES NEEDED FROM USER

CAPACITY FACTOR             (cf)    [% in decimal]
CAR CAPACITY                (cc)    [kg]
NUMBER OF FLOORS
- population per floor      (ui)
- height of each floor      (df)    [m]
DOOR OPEN TIME              (to)    [s]
DOOR CLOSE TIME             (tc)    [s]
PASSENGER LOADING TIME      (tl)    [s]
PASSENGER UNLOADING TIME    (tu)    [s]
CONTRACT SPEED              (v)     [m/s]
NUMBER OF ELEVATORS         (L)
JERK                        (j)     [m/s/3]
ACCELERATION                (a)     [m/s/2]