###############################################################################
### This python script will produce a JFET common gate configuration        ###
### Fig.7.23(b)                                                            ###
### Page: 436                                                               ###
### Book: Electronic Devices and Circuit Theory                             ###
### By Robert L. Boylestad, Louis Nashelsky                                 ###
### 11th Edition                                                            ###
###############################################################################
### Student_Registration_Number: 2020338027                                 ###
###############################################################################

# Import the necessary libraries from schemdraw
import schemdraw
import schemdraw.elements as elm

# Create a drawing object
d = schemdraw.Drawing()
#Drawing configuration
d.config(unit=3)
# Add an input voltage label and dot
d += elm.Dot(radius=0.08, open=True).label("$ V_i $ ",'lft')

# Add a horizontal line
d += elm.Line().right().length(1)

# Add and label a capacitor (C1)
d += elm.Capacitor2().reverse().length(1).right().label('$C_1$').flip()  # Flip the first capacitor

# Add a horizontal line
d += elm.Line().right().length(1)

# Push the drawing context to add components in a different vertical position
d.push()

# Add and label a resistor (R_S) and a battery (V_SS)
d += elm.Resistor().length(2).down().label('$R_S$')
d += elm.Battery().length(2).down().reverse().label('$V_{SS}$').label('+',ofst=(0.5,0)).label('_',ofst=(-0.5,0))

# Add a ground symbol
d += elm.Ground()

# Pop the drawing context to return to the previous vertical position
d.pop()

# Add a horizontal line
d += elm.Line().right().length(2)

# Add and label a JFET (common gate configuration) with a skyblue circle behind it
d.push()
d += elm.JFetP(circle='m',fill='skyblue', color='none').down().flip().label("$I_{DSS}$", ofst=-2.45).label("$V_{P}$", ofst=-2.05)
d.pop()
d += elm.JFetP().down().flip().label("$I_{DSS}$", ofst=-2.45).label("$V_{P}$", ofst=-2.05)
# Add a small skyblue rectangle at a specific position
d += elm.Rect(dx=.001, dy=.001, fill="skyblue", color="none").at((5.2,1.7))
# Add labels for the JFET terminals (G, S, D)
d += elm.Dot().label('G').down().at((5.90,-1.39))
d += elm.Dot().label('S').left().at((4.418,-0.013))
d += elm.Dot().label('D').left().at((6.88,0.006))

# Add connecting lines and a ground symbol
d += elm.Line().at((5.91, -0.61)).length(3.4)
d += elm.Ground()
d += elm.Line().length(2.3).right().at((6.211, -0.001))

# Push the drawing context again to add components in a different vertical position
d.push()

# Add and label a resistor (R_D) and a battery (V_DD)
d += elm.Resistor().length(2).down().label('$R_D$','bot')
d += elm.Battery().length(2).down().label('$V_{DD}$','bot').label('_',ofst=(0.4,0.8)).label('+',ofst=(-0.4,0.8))

# Add a ground symbol
d += elm.Ground()

# Pop the drawing context to return to the previous vertical position
d.pop()

# Add and label a capacitor (C2)
d += elm.Capacitor2().length(3).right().label('$C_2$')

# Add an output voltage label and dot
d += elm.Dot(radius=0.08, open=True).label("$ Vo $ ",'rgt')

# Save the drawing as a PDF file
d.save('Fig7.23(b)_ElecDevice_RBoylstadPg436_11E.pdf')

# Draw the complete circuit
d.draw()
