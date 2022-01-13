from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

def hello_world(request):
    medicines =  [
  {
    'id':12, 
    'name':"Panadol Extra Tablets 20's",
    'category':"Pain Relief",
    'reqPrescription': False,
    'description':"Panadol Extra contains Paracetamol 500mg and Caffeine 65mg. A mild analgesic and antipyretic formulated to give extra pain relief. The tablets are recommended for the treatment of most painful and febrile conditions, headache, including migraine, backache, toothache, rheumatic pain and dysmenorrhoea, and the relief of the symptoms of colds",
    'quantity':23,
    'price': 100,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/83b49b60-d48f-4c27-92d2-47a5f580c6dc.JPG"
  },
{
    'id':1, 
    'name':"Almax Forte Sachets 30's",
    'category':"Acid Reflux and Peptic Ulcers",
    'reqPrescription': False,
    'description':"ALMAX FORTE 1.5 G 24 SACHETS ORAL SUSPENSION",
    'quantity':23,
    'price': 1220,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/b1d156b6-2c4c-4c12-b430-b435b68de9bd.JPG"
  },

{
    'id':123, 
    'name':"Evolve Carmellose Eye Drops 10ml",
    'category':"Eye Drops",
    'reqPrescription': True,
    'description':"Evolve Carmellose Eye Drops is a soothing eye drops medication indicated to provide relief arising from discomfort caused by dry eye sensations.",   
    'quantity':23,
    'price': 1200,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/6c4016d3-052d-4016-9d09-2bac8f041708.JPG"
  },

{
    'id':134, 
    'name':"Alatrol Syrup 5mg/5ml 60ml",
    'category':"Allergy-relief",
    'reqPrescription': True,
    'description':"Alatrol Syrup contains Cetirizine which is an antihistamine used to relieve allergy symptoms such as watery eyes, runny nose, itching eyes/nose, sneezing, hives, and itching. It works by blocking a certain natural substance (histamine) that your body makes during an allergic reaction.",
    'quantity':3,
    'price': 120,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/d5d78f00-b33b-409b-9e75-ecea1ac45325.JPG"
  },

{
    'id':56, 
    'name':"Coldcap Day Time & Night Time Co-Pack 24's",
    'category':"Respiratory relief",
    'reqPrescription': True,
    'description':"Coldcap Day time and Night time contains Paracetamol 500mg,Caffeine 30mg,Pseudoephedrine 30mg per Coldcap Day Time capsule and Paracetamol 500mg, Chlorpheniramine 4mg per Coldcap Night Time capsule.Coldcap .Day Time and Night time is used to temporarily treat symptoms caused by the common cold, flu, allergies,sinusitis, bronchitis.It also helps relieve stuffy nose, sinus, and ear congestion symptoms. Paracetamol will relieve pain and fever while the antihistamine(Chlorpheniramine) helps relieve watery eyes, itchy eyes/nose/throat, runny nose, and sneezing.",
    'quantity':78,
    'price': 170,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/0f32fd41-4bde-46b1-89b0-ef146239770c.JPG"
  },

{
    'id':176, 
    'name':"Postinor 2 Tablets 2's",
    'category':"Emergency Contraceptives",
    'reqPrescription': False,
    'description':"Postinor-2 also known as P2 contains the active ingredient levonorgestrel. It is commonly known as the morning after pill, used only as an emergency contraceptive. It is used to prevent pregnancy when taken within 72 hours (3 days) of unprotected intercourse/sex.",
    'quantity':3,
    'price': 160,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/398efbb9-57ca-4fb9-ba66-fc9f0fc45eed.JPG"
  },

{
    'id':16, 
    'name':"Kwells 30mcg Adult Tablets 12's",
    'category':"Anti-nauseants",
    'reqPrescription': False,
    'description':"Kwells travel sickness tablets provide fast, effective relief of travel sickness. Pack of 12 melt in the mouth tablets. It contains Hyoscine hydrobromide, that acts on the balance organs of the inner ear and on the nerves responsible for nausea. Because Kwells Kids tablets melt in the mouth, absorption into the bloodstream is very rapid.",
    'quantity':3,
    'price': 580,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/77c3102d-f21e-40ed-9ef9-52a64feee2a7.JPG"
  },

{
    'id':160, 
    'name':"Panadol Baby& Infant Suspension 100ml",
    'category':"Pain Relief",
    'reqPrescription': False,
    'description':"Panadol Baby & Infant contains Paracetamol 120mg in each 5 ml. Paracetamol is an antipyretic (fever reliever) and analgesic (pain reliever). It helps in relieving pain of teething,sore throat and fever associated with colds and flu, childhood infections like chicken pox, whooping cough, measles and mumps.",
    'quantity':39,
    'price': 320,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/9127a3ef-5938-4e70-83f7-32f7eaff8f34.JPG"
  },

{
    'id':190, 
    'name':"Cital Syrup 100ml",
    'category':"Acid Reflux and Peptic Ulcers",
    'reqPrescription': False,
    'description':"Cital Oral Liquid Sugar Free Sugar Free is a urine alkalizer. It works by increasing the pH of urine which makes it less acidic. This helps the kidneys get rid of excess uric acid, thereby preventing gout and certain types of kidney stones.",
    'quantity':39,
    'price': 230,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/e4d6d0f3-8d62-46dd-b786-4c3c61b315cb.JPG"
  },
{
    'id':48, 
    'name':"Benadryl Allergy Relief Capsule 12's",
    'category':"Allergy-relief",
    'reqPrescription': True,
    'description':"Benadryl Allergy Relief is indicated for the symptomatic relief of allergic rhinitis, including hay fever. Benadryl Allergy Relief is also indicated for chronic idiopathic urticaria. Benadryl Allergy Relief contains 8 mg Acrivastine per capsule.Excipient with known effect: Lactose 206.80 mg per capsule.",
    'quantity':39,
    'price': 1000,
    'availability':True,
    'imageUrl':"https://media.mydawa.com/Images/Products/44489c39-5bfc-405e-b575-83156cff43bb.JPG"
  }

]
    return JsonResponse({'medicines':medicines})

# Create your views here.
