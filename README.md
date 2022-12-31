# condorcet_calculator

## Technical Description
A calculator that takes in ordinal voter preferences and returns a directed graph of preference orderings. Terminal nodes indicate strong and weak Condorcet winners. Directed graph also shows any potential transitive group preferences.

## Background
Individual people have, what political scientists and economists often refer to, what are called "intransitive preferences," meaning their preferences do not circle back to the beginning. For example, let's talk icecream. Pretty much everyone has a favorite icecreams, some less preferred flavors, and a least favorite. Let's say you like vanilla > chocolate > strawberry. This is your preference ordering. And this preference ordering is intransitive because you can't loop back to vanilla from strawberry. The preference ordering simply ends, therefore it is intransitive.

Now, what about groups? Let's say person 1 has vanilla > chocolate > strawberry, perseon 2 has chocolate > strawberry > vanilla, and person three has strawberry > vanilla > chocolate. Now, at the GROUP level, what is the preference ordering? Well, each option, vanilla, chocolate, and strawberry, each come in first place once, second place once, and third place once. So there's no clear winner. At the group level, these preference orderings are colletively transitive. We CAN circle back to the beginning.

In politics, group preferences are understood to be much more complicated than individual preferences. Aggregating preferences is possibly the biggest problem in studying any voting system: discoveries like Arrows Theorem teach us that there is no such voting system that can fairly aggregate preferences 100% of the time. 

The tool included here is a calculator that shows a directed graph of group preferences. It calculates the condorcet winner, which is a topic I can't properly explain in a readme and I encourage you to look up on Wikipedia. Essentially, it's the election results if you take all of the voters and ask "What would this eletion look like if I had these voters vote on only two options at a time?" From there, these pairwise victories are added to a database and a graph is made of the pairwise victories. Follow the arrows to a terminal node to find a condorcet winner. If there is no terminal node there is no condorcet winner. If two terminal nodes are connected to each other by an edge with 0, that means the group is indifferent between the two of them.

## How to run
The python script uses an argparser and can be run from the command line. Simply set your working directory and type $ python VPGv8.py csv_name_here.csv and see your results. You will need numpy, pandas, networkx, matplotlib, and argparse available. Built using python 30.10.8 in visual studio code. The code is heavily annotated so I hope you can take something away from it!
