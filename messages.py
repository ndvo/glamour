# -*- coding: utf-8 -*-
#!/usr/bin/env python

import gettext
t = gettext.translation("glamour", "locale")
_ = t.ugettext

enemy = {
        "birdy": _("Look, it's a small BIRDY! It's so small and so cute... it also sings oh so happy. Don't you bother it much, though... it won't like it."),
        "butterflies": _("Oh, oh! Look... BUTTERFLIES! Have you ever seen anything oh so pretty? Don't you waste too much time celebrating their beauty, though - we have a ball to attend."),
        "carriage": _("Well, the path is blocked by a CARRIAGE. They are beautiful transportation, all right, but are oh so slow... maybe we ought to find another path."),
        "elephant": _("Look, a baby loxodonta africana! Well, most people would just call it an ELEPHANT. It's oh so rude. They are cute, intelligent animals with the niftiest ears."),
        "footboy": _("Oh, sheesh! There goes Fabrizio and his soccer ball. BOYS are so careless when they're playing. Watch out or he may get you dirty."),
        "giraffe": _("A giraffa camelopardalis! People thought they were legend, and you can totally see why: so many dots, so many horns and oh so much neck. GIRAFFES are kinda cute, don't you think?"),
        "hawk": _("My, oh my! You disturbed that fellow birdy, didn't you? Now here comes her MOMMY BIRD and she's not happy... would you care to run?"),
        "lion": _("Oh, I just love panthera leos - or LIONS, if you must. They are just big, fat, cute kittys for me, but I guess you people are oh so scared of them, right? Maybe a little kindness would help."),
        "monkey": _("Watch out for that green, furry little kid up there! Oh, it's a MONKEY, you say? He seems not nice. I wonder why he has so many bananas..."),
        "old lady": _("Oh, it's MRS KLEENER. It's oh so nice to see someone cleaning and taking care of things. She deserves a kiss, but watch out for the dust."),
        "penguin": _("Hey, what's that? Oh it is a fat, cute flightless bird. They call it a PENGUIN - it's a smart, friendly, stable and virus free bird with lots of great open software avaiable. Wait, am I confusing the bird with the OS? Ah, whatever, both are just great!"),
        "schnauzer": _("Oh, what a cute little fellow, that dog! Wait, it's also appears oh so mad. SCHNAUZERS may be a little angry, but they sure love a little kindness."),
        "viking ship": _("My, oh my! A VIKING SHIP! The old norse would travel anywhere on these, but you wouldn't want to listen to their filthy language. They don't care much for kindness or cuteness either, so why won't we just leave, uh? Please?")
    }

place = {
        "bathhouse": _("Look, princess, it's a BATHHOUSE! When you get dirty, you should come here to clean yourself. You wouldn't want to attend the ball filthy, would you?"),
        "accessory hall": _("Wow! Don't you just love accessories? Here, in the ACCESSORY HALL, you'll be able to decorate yourself up so you look astonishing. Many people here prefer swords and shields, but as for me, I think strenght lies on cute ribbons and cool shades."),
        "cinderellas castle": _("This is CINDERELLA'S CASTLE. It is oh so big and classy. Let's go inside say hello, and maybe ask what she will wear to the next ball. It is always bad to show up with the same clothes."),
        "drains": _("Eew! These DRAINS take away the dirty water, leaving streets dry and clean. Please don't bathe on that water, or you'll get filthy. Be careful!"),
        "dress tower": _("All girls dream of coming to the DRESS TOWER. Here you will find all sorts of chic and marvelous dresses. Bet you'll take your time checking them out, right?"),
        "gateway": _("This is a GATEWAY, connecting different streets on the city. Don't forget to use them to visit every street you can. Oh, it is just so exciting to visit new places!"),
        "maddelines house": _("Well, as you know, this is YOUR CASTLE. You may return here if you are really impatient to go to the ball, and also to see what were you wearing last night, so you don't repeat yourself."),
        "magic beauty parlor": _("Princess, look! That's my favourite building - the MAGIC BEAUTY SALON! At it, you'll be able to change haircuts, and even skin tone. I don't really know how they do it... maybe that's why it's magical. It won't help you earn any glamour, though."),
        "make-up tower": _("I just love make-up, but you totally can't tell, right? That's because I get it on the MAKE-UP TOWER, where all cosmetics are oh so great and magical! You can look like another person with them, but you young girls don't even need it, do you?"),
        "rapunzels villa": _("That's RAPUNZEL'S VILLA. She prefer ground buildings after all those towers incidents, you know? I totally envy her hair, but I guess we could drop by and say hello."),
        "shoes shop": _("My oh my, look at those shoes! I know I can fly, but I like style and fashion too, you know? I wouldn't mind if you decided to spend some quality time in the SHOE'S SHOP, really. You can thank me later."),
        "sleeping beautys palace": _("If this is SLEEPING BEAUTY'S PALACE, you ask? Of course, but you can call her Talia. You can tell she's oh so elegant and chic by her home, can't you? Let's go in - maybe she has some tips on what you should wear."),
        "snow-whites castle": _("Isn't SNOW WHITE'S CASTLE oh so cute and cozy? Let's go meet her, for she is my favourite princess in the whole world... except for you dearie, of course."),
        "zoo": _("Look, look, a ZOO! Oh, I just love to see all kinds of animals that share this world with us. They are oh so cute and lovely. I'd prefer if they were free in the wild, but then I wouldn't get to see them, I suppose. Keep your eyes on them.")
        }

event   = {
        "dirty": _("Ouch! Look, princess, you and your dress are now a little dirty. Getting to the ball dirty will make you lose some glamour, so try to keep yourself... higienic, ok?"),
        "dirty 2": _("Watch out, dearie! You got even dirtier, and I would suggest you cleaned yourself up before the ball, ok? Why don't you look for the Bathhouse?"),
        "dirty 3": _("Come on, princess! You are now as dirty as it gets. Going to the ball like this would be oh so embarassing. No way... uh, uh. Go take a bath and stop getting filthy my little piggy princess."),
        "save game": _("You can save your game by pausing and selecting the Save Game option. Neat, huh? This way you can resume from where you left off, and keep you glamour score. Ahh... technology if just great!"),
        "day start 1": _("Hello again, princess! We have much to see and wear before the ball tonight. Let's get going, becouse today you will rock the ball! He, he, I always wanted to say that."),
        "day start 2": _("My, oh my, princess! I think you overslept. Let us go already, I have so many dresses and shoes to try on. Oh, I mean... 'you' have many things to try on."),
        "day start 3": _("Did you see those boys in the ball? They are all so cute and handsome when not covered in mud and chasing a football. Oh, if I were a young fairy again..."),
        "day start 4": _("New day, new hope. Maybe we can make you prettier than Snow White today... oh she's so pretty. I mean... you are so pretty also!"),
        "day start 5": _("Hello, dearie! I'm happy because I danced all night yesterday... I bet you love valse, but you have not really tasted it until you do it flying."),
        "day start 6": _("Good morning, dearie! My, you look so pretty already. It's a shame you can't wear that again tonight. Why not? Well, because a glamorous woman should not repeat her outfit twice in a row. Hey! What's that about my outfit...!?"),
        "day start 7": _("All right, all right! I 'will' take you to see new shoes, but only if today we go see those new fairy wands. I hear they are great..."),
        "day start 8": _("Hi, sweetie! You know, in the old days I would just make you an outfit out of mice and pumpkins, but I was threatened with a lawsuit, do you believe that? These goofy, phony property rules are just killing creativity."),
        "day start 9": _("Hello, my little princess. You keep getting prettier with each passing day. I wish I was that much pretty, but I think I'll just have to be satisfed with my magic powers, flight ability and immortality."),
        "day start 10": _("Good morning, sweetie! You did look wonderful last ball, but with a few more time and training, I bet you'll just explode with glamour. Oh, no, it doesn't hurt, sweetie, I swear."),
        "day start 11": _("Hi, cutie face! You sure are glamorous enough for nobility, but want to test yourself against royalty? Maybe, some day, you'll even be a match for the fae."),
        "day start 12": _("Ok, ok. I get it... But another ball, really? Don't you want to try someting different tonight? Maybe bowling..."),
        "day start 13": _("Hi, princess! You noticed the queen did not attend the last ball? Her magic mirror was unstable and crashing all the time, poor thing. If she had that penguin OS on it, she wouldn't have those problems. Wonder if the kernel supports divination well."),
        "day start 14": _("Hello, cutest! Great ball last night, but the valse was rather lowsy. Maybe if they looked for music in jamendo.com... Oh, there are oh so many great bands there, as Ehma, Torley on Piano, Ceili Moss, Armolithae and Butterfly Tea. My oh my!")
        }


intro = {
        "first day a": _("Good morning, princess, and an oh so happy birthday, too! I can't believe you turned 16 already, and in such a beautiful day, too! Of course, now that that you're a lady, you should start attending the royal balls... oh, it'll be so exciting."),
        "first day b": _("For these balls, you'll get to dress up elegantly, match your outfit, wear make-up and dresses. Oh, I'm so jealous. You'll get to be really, really beautiful. Well, surely you look oh so beautiful already, no doubt about it..."),
        "first day c": _("...but you know, that is not enough for the royal balls. For them, you'll have to be glamourous! Since it is your first ball ever, I was assigned to assist you in getting lovely, glamorous and stunning. And getting the hearts of the boys, too."),
        "first day d": _("You see, for every ball you should try to dress up wonderfully, which means selecting a nice DRESS, SHOES, MAKE-UP and ACCESSORY. You should wander around the city looking for them, and putting on those you like the best."),
        "first day e": _("Of course, other princesses are attending the ball, too, so you should try to avoid showing up with the same things they do. Pay them a visit to learn what they will be wearing, and also try to avoid using the same outfit two balls in a row."),
        "first day f": _("But caution, many dangers await! Well, not 'real' dangers, but there are many ways to get yourself dirty before the ball, and you should avoid that. Clean yourself at the bathhouse if you need, and use you cursor and irresistable kisses to help you keep clean."),
        "first day g": _("At the ball, you'll gain glamour points if your outfit differs from the other princesses', and you'll lose them if it doesn't. You'll loose an awful lot of glamour if you're dirty, so watch out. Uh, what...? What is glamour for, you ask?"),
        "first day h": _("Oh, silly princess. Glamour is just... beautiful and divine. Ah, yes, it also draws the eyes and hearts of boys, although high-ranked nobility tends to be more used to it than lower rank. But I assure you even Prince Charming can fall for a glamorous girl."),
        "first day i": _("So let's get started, turning you from a cute, loving little princess into a wonderful, glamorous little princess. I'll be helping you on the way, so off we go.")
        }
