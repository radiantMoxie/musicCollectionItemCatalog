from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Base, Artist, Album, User

engine = create_engine('sqlite:///musiccollection.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)
session = DBSession()

# Create dummy user
user1 = User(name="Yana Kesala", email="yana.kesala@gmail.com", id = 1)
session.add(user1)
session.commit()

user2 = User(name='Radiant Moxie', email = 'radiant.moxie@gmail.com', id = 2)
session.add(user2)
session.commit()

#Albums for Sting
artist1 = Artist(user_id=1, name = 'Sting', picture = '/static/Sting.jpg')

session.add(artist1)
session.commit()

album1 = Album(name = 'Brand New Day', description = \
	"From AllMusic.com:\
	By the late '90s, Sting had reached a point where he didn't have to prove \
	his worth every time out; \
	he had so ingrained himself in pop culture, he really had the freedom to \
	do whatever he wanted. \
	He had that attitude on Mercury Falling, but it was too somber and serious,\
	 everything that its successor, \
	Brand New Day, is not. Light, even effervescent, Brand New Day feels like \
	little else in Sting's catalog. \
	Not that it represents a new beginning, contrary to what the title may \
	promise. \
	The album is not only firmly within his tradition, it sounds out of time \
	-- it's odd how close \
	Brand New Day comes to feeling like a sequel to Nothing Like the Sun. \
	Musically, that is. \
	The sparkling, meticulous production and the very tone of the music -- \
	ranging from light funk to \
	mellow ballads to the Lyle Lovett tribute 'Fill Her Up' -- are of a piece \
	with Sting's late-'80s work. \
	That's the main thing separating it from Ten Summoner's Tales, his other \
	straight pop album -- \
	well, that, and the levity. There are no overarching themes, no political \
	messages on Brand New Day \
	-- only love songs, story songs, and, for lack of a better term, \
	inspirational exhortations. \
	This is all a good thing, since by keeping things light he's managed to \
	craft an appealing, engaging record. \
	It may not ask as much from its audience as Sting's other '90s efforts, \
	but it's immediately enjoyable, \
	which isn't the case for its cousins. Brand New Day doesn't boast any new \
	classics, \
	and it does sound a little dated, but it's well-crafted, melodic, and has \
	a good sense of humor -- \
	exactly the kind of record Sting should be making as he embarks on the \
	third decade of his career.", 
	year_released = 1999, artist = artist1, picture = '/static/BrandNewDay.jpg',
	user_id = 1)

session.add(album1)
session.commit()

album2 = Album(name = 'The Dream of the Blue Turtles', description = \
	"From AllMusic.com:\
	Sting had a lot to prove on his first post-Police effort, and he proved \
	himself up to the task of \
	establishing a distinctive identity as a solo artist. Instead of \
	replicating his reggae-tinged Police \
	style, he ventured into new realms, hiring top drawer American jazz \
	musicians like Branford Marsalis, \
	Kenny Kirkland and drum monster Omar Hakim to accompany him on the kind \
	of harmonically sophisticated \
	(though decidedly non-jazz) tunes he'd begun working on towards the end \
	of the Police's lifetime \
	(see SYNCHRONICITY). There's still a touch of reggae on the open-hearted \
	'Love Is the Seventh Wave,' \
	and even a funked-up version of the formerly abstract Police tune 'Shadows \
	In The Rain,'' but most of \
	the tunes here (except the pop smash 'If You Love Somebody Set Them Free' \
		are the kind of literate, \
	adult-friendly sophisto-pop that would become a template for his \
	subsequent solo recordings. \
	BLUE TURTLES still stands as one of his most memorable albums.", 
	year_released = 1985, artist = artist1, 
	picture = '/static/DreamTurtles.jpg', user_id = 1)

session.add(album2)
session.commit()

album3 = Album(name = 'Nothing Like the Sun', description = \
	"From AllMusic.com:\
	If Dream of the Blue Turtles was an unabashedly pretentious affair, it \
	looks positively lighthearted \
	in comparison to Sting's sophomore effort, Nothing Like the Sun, one of \
	the most doggedly serious pop \
	albums ever recorded. This is an album where the only up-tempo track, the \
	only trifle -- the cheerfully \
	stiff white-funk 'We'll Be Together' -- was added at the insistence of \
	the label because they believed \
	there wasn't a cut on the record that could be pulled as a single, one \
	that would break down the doors \
	to mainstream radio. And they were right, since everything else here is \
	too measured, calm, and \
	deliberately subtle to be immediate (including the intentional throwaway, \
	'Rock Steady'). So, why is it \
	a better album than its predecessor? Because Sting doesn't seem to be \
	trying so hard. It flows naturally, \
	largely because this isn't trying to explicitly be a jazz-rock record \
	(thank the presence of a new rhythm \
	section of Sting and drummer Manu Katche for that) and because the \
	melodies are insinuating, slowly \
	working their way into memory, while the entire record plays like a \
	mood piece -- playing equally well \
	as background music or as intensive, serious listening. Sting's words \
	can still grate -- the stifling \
	pompousness of 'History Will Teach Us Nothing' the clearest example, \
	yet calls of 'Hey Mr. Pinochet' also \
	strike an uneasy chord -- but his lyricism shines on 'The Lazarus Heart,' \
	'Be Still My Beating Heart, \
	'They Dance Alone, and 'Fragile, a quartet of his very finest songs. \
	If Nothing Like the Sun runs a \
	little too long, with only his Gil Evans-assisted cover of 'Little Wing' \
	standing out in the final \
	quarter, it still maintains its tone until the end and, since it's buoyed \
	by those previously mentioned \
	stunners, it's one of his better albums.", year_released =1987, 
	artist = artist1, picture = '/static/NothingSun.jpg', user_id = 1)

session.add(album3)
session.commit()

#Albums for Gwen Stefani
artist2 = Artist(user_id=2, name = 'Gwen Stefani', picture = '/static/Gwen.jpg')

session.add(artist2)
session.commit()

album1 = Album(name = 'Love.Angel.Music.Baby', description = \
	"From AllMusic.com:\
	In the wake of Gwen Stefani's elevation to diva status in the early 2000s, \
	it's easy to forget that for \
	a brief moment at the start of the millennium it seemed that she and her \
	band, No Doubt, were \
	dangerously close to being pegged as yet another of the one-album alt-rock \
	wonders of the '90s. \
	Return of Saturn, their long-awaited 2000 follow-up to their blockbuster \
	1995 breakthrough Tragic Kingdom, \
	failed to ignite any sparks at either retail or radio, despite receiving \
	some strong reviews, and the \
	group seemed on the verge of disappearing. Then, Gwen sang on Eve's \
	'Let Me Blow Ya Mind' in 2001. \
	The Dr. Dre-produced song was a brilliant single, driven by a G-funk \
	groove and a sultry pop chorus \
	delivered by Stefani, and it was an enormous hit, peaking at number two on \
	the Billboard charts and \
	winning a Grammy, while redefining Gwen's image in the process. No longer \
	the cute SoCal ska-punk kid \
	of Tragic Kingdom, she was a sexy, glamorous club queen, and No Doubt's \
	next album, 2001's Rock Steady, \
	not only reflected this extreme makeover, it benefited from it, since her \
	new ghetto-fabulous persona \
	turned the album into a big hit. A side effect of this was that Gwen now \
	had a higher profile than her \
	band, making a solo album somewhat inevitable. Since she always dominated \
	No Doubt -- she was their face, \
	voice, lyricist, and sex symbol, after all -- it's reasonable to ask \
	whether vanity was the only reason \
	she wanted to break out on her own, since it seemed to the outside \
	observer that she helped set the \
	musical course for the band. A quick listen to Love.Angel.Music.Baby., \
	her 2004 solo debut, reveals \
	that this is not an album she could have made with the group -- it's too \
	club-centric, \
	too fashion-obsessed, too willfully weird to be a No Doubt album. Working \
	with far too many \
	collaborators -- including Dr. Dre, the Neptunes, Linda Perry, Dallas \
	Austin, Andre 3000, Nellee Hooper, \
	Jimmy Jam & Terry Lewis, and her No Doubt bandmate (and ex-boyfriend) \
	Tony Kanal -- Stefani has \
	created a garish, neon-colored, deliberately stylish solo album that's \
	intermittently exciting and \
	embarrassing. It covers far too much ground to be coherent, but a large \
	part of its charm is to hear \
	it careen from the thumping, minimal beats of the Neptunes-helmed \
	'Hollaback Girl' to the sleek, new \
	wave textures of the high school anthem-in-waiting 'Cool' and back to the \
	exhilarating freakazoid \
	sex song 'Bubble Pop Electric,'' featuring Andre 3000's alter ego Johnny \
	Vulture. This is music that \
	exists entirely on the surface -- so much so, that when Andre drops in \
	Martin Luther King samples \
	into the closer, 'Long Way to Go,'' it's a jarring buzz kill -- and that's \
	what's appealing about \
	L.A.M.B., even if it is such a shallow celebration of fleeting style and \
	outdated bling-bling culture, \
	it can grate. This shallowness can result in intoxicating beats, hooks, \
	and melodies, but also a fair \
	share of embarrassments, from odes to 'hydroponic love' and choruses built \
	on either 'That's my s*it' or \
	'take a chance, you stupid ho' to the stumbling contributions from Linda \
	Perry. But Stefani's dogged \
	desire to cobble together her own patchwork style while adhering to both \
	her new wave chick and urban \
	goddess personas can be both fascinatingly odd (her weirdly homoerotic \
		tribute to 'Harajuku Girls') and \
	irresistible. It's telling that the best moments on the album keep closest \
	to her new wave roots \
	(which include heavy electro synth beats and blips): no matter how hard \
	she tries, she is not a cultural \
	trailblazer like Madonna. Unlike Madge, she willingly adapts to her \
	collaborators instead of forcing them \
	to adapt to her, which means that L.A.M.B. truly does sound like the work \
	of seven different producers \
	instead of one strong-willed artist. Nevertheless, even if it doesn't \
	work all the time -- and some of \
	its best tracks still have moments that induce a withering cringe -- it's \
	a glitzy, wild ride that's \
	stranger and often more entertaining than nearly any other mainstream \
	pop album of 2004.", \
	year_released = 2004, artist = artist2, picture = '/static/LAMB.jpg',
	user_id = 2)

session.add(album1)
session.commit()

album2 = Album(name = 'The Sweet Escape', description = \
	"From AllMusic.com:\
	Awkward and alluring in equal measures, Gwen Stefani's 2004 solo debut, \
	Love.Angel.Music.Baby., did \
	its job: it made Gwen a bigger star on her own than she was as the lead \
	singer of No Doubt. With that \
	established and her long-desired wish for a baby finally fulfilled, there \
	was no rush for Gwen to get \
	back to her regular gig, so she made another solo album, The Sweet Escape, \
	which expanded on what really\
	sold her debut: her tenuous connections to Californian club culture. There \
	was always a sense of \
	artifice behind the turn-of-the-century makeover that brought Gwen from a \
	ska-punk sweetheart to a \
	dance club queen, but that doesn't mean it didn't work at least on \
	occasion, most spectacularly so on \
	the gloriously dumb marching-band rap of 'Hollaback Girl, the Neptunes \
	production that turned \
	L.A.M.B. into a blockbuster. There, as on her duet with Eve on \
	'Let Me Blow Ya Mind, Gwen made the \
	transition into a modern-day material girl with ease, but when she tried \
	to shoehorn this \
	ghetto-fabulous persona into her original new wave girl character, it felt \
	forced, nowhere more so \
	than on the Linda Perry written and produced 'What You Waiting For. \
	Gwen doesn't make that mistake \
	again on The Sweet Escape -- by and large, she keeps these two sides of \
	her personality separate, \
	favoring the streets and nightclubs to the comfort of her new wave home. \
	Just because she wants to \
	run in the streets doesn't mean she belongs there; she continues to sound \
	far more comfortable mining \
	new wave pop, as only a child of the '80s could. As always, it's those \
	celebrations of cool synths and \
	stylish pop hooks that work the best for Stefani, whether she's \
	approximating the chilliness of \
	early-MTV new romantics on 'Wonderful Life, mashing Prince and Madonna \
	on 'Fluorescent, or lying \
	back on the coolly sensual '4 in the Morning.'Only once on the album is \
	she able to bring this style \
	and popcraft to a heavy dance track, and that's on the irresistible \
	Akon-produced title track, \
	driven by a giddy 'wee-oh!' hook and supported by a nearly anthemic \
	summertime chorus. Tellingly, \
	the Neptunes, the architects of her best dance cuts on L.A.M.B., did not \
	produce this track, but they \
	do have a huge presence on The Sweet Escape, helming five of the 12 songs, \
	all but one being tracks \
	that weigh down the album considerably. The exception is 'U Started It, \
	a light and nifty evocation \
	of mid-period Prince, with its lilting melody, silken harmonies, and \
	pizzicato strings. It sounds \
	effortless and effervescent, two words that do not apply to their other \
	four productions, all skeletal, \
	rhythm-heavy tracks that fail to click. Sometimes, they're merely leaden, \
	as on the stumbling \
	autobiographical rap 'Orange County Girl'; sometimes, they're cloying and \
	crass, as on the rather \
	embarrassing 'Yummy'; sometimes they have an interesting idea executed \
	poorly, as on 'Breakin' Up, a \
	breakup song built on a dying cell phone metaphor that's interesting in \
	theory but its stuttering, \
	static rhythms and repetitive chorus are irritating in practice. Also \
	interesting in theory is the \
	truly bizarre lead single, 'Wind It Up,' where the Neptunes force fanfares \
	and samples from The Sound \
	of Music's 'The Lonely Goatherd' into one of their typical minimalist \
	tracks, over which Gwen spouts \
	off clumsy material-minded lyrics touting her fashion line and her shape. \
	Nothing in this track really \
	works, but it's hard not to listen to it in wonder, since its unwieldy \
	rhythms and rhymes capture \
	everything that's currently wrong about Stefani. From the stilted \
	production to the fashion fetish, \
	all the way down to her decision to rap on far too much of the album, \
	all the dance-pop here seems \
	like a pose, creating the impression that she's a glamour girl slumming \
	on a weekend night -- something \
	that her self-proclaimed Michelle Pfieffer in Scarface 'coke whore' \
	makeover showcased on the album's \
	cover doesn't do much to dissuade. If the dance production on The Sweet \
	Escape were better, \
	these hipster affectations would be easier to forgive, but they're not: \
	they're canned and bland, \
	which only accentuates Stefani's stiffness. These misfires are so grand \
	they overshadow the many good \
	moments on The Sweet Escape, which are invariably those songs that stay \
	true to her long-standing love \
	 f new wave pop (not coincidentally, these include every production from \
	 	her No Doubt bandmate \
	Tony Kanal). These are the moments that give The Sweet Escape its \
sweetness, and while they may \
	require a little effort to dig out, they're worth the effort, since it \
	proves that beneath the layers of \
	bling, Gwen remains the SoCal sweetheart that has always been as spunky \
	and likeable as she has been \
	sexy.", year_released = 2006, artist = artist2, user_id = 2,
	picture = '/static/Escape.jpg')

session.add(album2)
session.commit()

#Albums for Fiona Apple
artist3 = Artist(user_id=1, name = 'Fiona Apple', picture = '/static/Fiona.jpg')

session.add(artist3)
session.commit()

album1 = Album(name = 'Tidal', description = 
	"From AllMusic.com:\
	Fiona Apple demonstrates considerable talent on her debut album, Tidal, \
	but it is unformed, \
	unfocused talent. Her voice is surprisingly rich and supple for a \
	teenager, and her jazzy, \
	sophisticated piano playing also belies her age. Given the right material, \
	such talents could have \
	flourished, but she has concentrated on her own compositions, which are \
	nowhere near as impressive \
	as her musicianship. Most of Tidal is comprised of confessional \
	singer/songwriter material, and \
	while they strive to say something deep and important, much of the \
	lyrics settle for cliches. \
	Apple does have a handful of impressive songs on Tidal, like the haunting \
	'Shadowboxer' \
	and 'Sullen Girl, but the gap between her performing talents and \
	songwriting skills is too \
	large to make the album anything more than a promising, and very \
	intriguing, debut.", 
	year_released = 1996, artist = artist3, user_id = 1,
	picture = '/static/Tidal.jpg')

session.add(album1)
session.commit()

album2 = Album(name = 'When the Pawn...', description = 
	"From AllMusic.com:\
	Fiona Apple may have been grouped in with the other female \
	singer/songwriters who dominated the \
	pop charts in 1996 and 1997, but she stood out by virtue of her grand \
	ambitions and considerable \
	musical sophistication. Even though her 1996 debut Tidal occasionally \
	was hampered by naivete, it \
	showcased a gifted young artist in the process of finding her voice. \
	Even so, the artistic leap \
	between Tidal and its long-awaited 1999 sequel When the Pawn Hits... \
	is startling. It's evident \
	that not only have Apple's ambitions grown, so has her confidence -- \
	few artists would open \
	themselves up to the ridicule that comes with having a 90-word poem \
	function as the full title, \
	but that captures the fearless feeling of the record. Apple doesn't \
	break from the jazzy pop of \
	Tidal on Pawn, choosing instead to refine her sound and then expand its \
	horizons. Although there \
	are echoes of everything from Nina Simone to Aimee Mann on the record, \
	it's not easy to spot \
	specific influences, because this is truly an individual work. As a \
	songwriter, she balances her \
	words and melodies skillfully, no longer sounding self-conscious as she \
	crafts highly personal, \
	slightly cryptic songs that never sound precocious or insular. With \
	producer Jon Brion, she \
	created the ideal arrangements for these idiosyncratic songs, finding a \
	multi-layered sound \
	that's simultaneously elegant and carnival-esque. As a result, Pawn is \
	immediately grabbing, \
	and instead of fading upon further plays, it reveals more with each \
	listen, whether it's a \
	lyrical turn of phrase or an unexpected twist in the arrangement; what's \
	more, Apple has made \
	it as rich emotionally as it is musically. That's quite a feat for any \
	album, but it's doubly \
	impressive since it is only the second effort by a musician who is only \
	22 years old.", year_released = 1999, artist = artist3, user_id = 1,
	picture = '/static/Pawn.jpg')

session.add(album2)
session.commit()

album3 = Album(name = 'Extraordinary Machine', description = 
	"From AllMusic.com:\
	To say that the released version of Extraordinary Machine is a marked \
	improvement over \
	the bootlegged version is not to say that it sounds more complete -- \
	after all, the booted \
	Jon Brion productions sounded finished, as evidenced by the two cuts that \
	were retained; the \
	intricate chamber pop of the opening title track and the closing \
	'Waltz (Better Than Fine)' are \
	the only time Brion's productions not only suited, but enhanced Fiona \
	Apple's songs -- but they \
	are both more accessible, and more fully realized, letting Apple's songs \
	breathe in a way they \
	didn't on the original sessions. While Brion's productions were \
	interesting, they stretched his \
	carnivalesque aesthetic to the limit, ultimately obscuring Apple's songs, \
	which were already \
	fussier, artier, and more oblique than her previous work. When matched to \
	Brion's elaborately \
	detailed productions, her music became an impenetrable Wall of Sound, but \
	Mike Elizondo's \
	productions open these songs up, making it easier to hear Apple's songs \
	while retaining most of \
	her eccentricities. Now, Extraordinary Machine sounds like a brighter, \
	streamlined version of \
	When the Pawn, lacking the idiosyncratic arrangement and instrumentation \
	of that record, yet \
	retaining the artiness of the songs themselves. Like her second record, \
	this album is not immediate; \
	it takes time for the songs to sink in, to let the melodies unfold, and \
	decode her laborious words \
	(she still has the unfortunate tendency to overwrite: 'A voice once \
		stentorian is now again/Meek and \
	muffled'). Unlike the Brion-produced sessions, peeling away the layers \
on Extraordinary Machine is \
	not hard work, since it not only has a welcoming veneer, but there are \
	plenty of things that \
	capture the imagination upon first listen -- the pulsating piano on \
	'Get Him Back,' the moodiness \
	of 'O' Sailor, the coiled bluesy 'Better Version of Me,' the quiet \
	intensity of the breakup \
	saga 'Window,' the insistent chorus on 'Please Please Please'-- which \
	gives listeners a reason \
	to return and invest time in the album. And once they do go back for \
	repeated listens, \
	Extraordinary Machine becomes as rewarding, if not quite as distinctive, \
	as When the Pawn. \
	Nevertheless, this is neither a return to the sultry, searching \
	balladeering of Tidal, nor a \
	record that will bring her closer to tasteful, classy Norah Jones \
	territory, thereby making her \
	a more commercial artist again. Extraordinary Machine may be more \
	accessible, but it remains an \
	art-pop album in its attitude, intent, and presentation -- it's just \
	that the presentation is \
	cleaner, making her attitude appealing and her intent easier to ascertain, \
	and that's what makes \
	this final, finished Extraordinary Machine something pretty close to \
	extraordinary.", year_released = 2005, artist = artist3, user_id = 1,
	picture = '/static/EM.jpg')

session.add(album3)
session.commit()

print 'added albums!'