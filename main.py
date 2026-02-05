from crewai import Crew
from dotenv import load_dotenv
from agents import trichyagents
from tasks import trichytask

load_dotenv()

def main():
    # Get city input from user
    city = input("Enter your city name: ")
    
    # Initialize agents and tasks
    agents = trichyagents()
    tasks = trichytask()

    # Create agents
    print("Initializing agents...")
    holy_places = agents.holy_places()
    #jewellery_shop = agents.jewellery_shop()
    shopping_mart = agents.shopping_mart()
    #courier_service = agents.courier_service()
    #restaurant_analyst = agents.restaurant_analyst()
    #servicecenter_finder = agents.servicecenter_finder()
    #Homeapplst_finder = agents.Homeapplst_finder()
    #entertainment_agent = agents.entertainment_agent()
    #vessel_shop_agent = agents.vessel_shop_agent()  # Fixed: was calling entertainment_agent
    #stationary_shop_agent = agents.stationary_shop_agent()
    #photoshop_agent = agents.photoshop_agent()
    #hospital_analyst = agents.hospital_analyst()
    #companies = agents.companies()
    #furniture_shop = agents.furniture_shop()
    #gift_shop = agents.gift_shop()
    #textile = agents.textile()
    #parlour = agents.Parlour()
    #institute = agents.institute()
    #tour = agents.tour()
    #room_analyst = agents.room_analyst()

    # Create tasks
    print("Creating tasks...")
    holy_place_searcher = tasks.holy_place_searcher(holy_places)
    #Jewellery_finder = tasks.Jewellery_finder(jewellery_shop)
    mart_seracher = tasks.mart_seracher(shopping_mart)
    #courier_finder = tasks.courier_finder(courier_service)
    #restaurant_suggest = tasks.restaurant_suggest(restaurant_analyst)
    #suggest_auto = tasks.suggest_auto(servicecenter_finder)
    #suggest_homeappl = tasks.suggest_homeappl(Homeapplst_finder)
    #entertainment_task = tasks.entertainment_task(entertainment_agent)
    #vessel_shop_task = tasks.vessel_shop_task(vessel_shop_agent)
    #stationary_shop_task = tasks.stationary_shop_task(stationary_shop_agent)
    #photoshop_task = tasks.photoshop_task(photoshop_agent)
    #hospital_suggester = tasks.hospital_suggester(hospital_analyst)
    #finding_IT_companies = tasks.finding_IT_companies(companies)
    #finding_Automobiles_companies = tasks.finding_Automobiles_companies(companies)
    #locating_display_furniture = tasks.locating_display_furniture(furniture_shop)
    #discovering_gift_shops = tasks.discovering_gift_shops(gift_shop)
    #text_task = tasks.text_task(textile)
    #par_task = tasks.par_task(parlour)
    #skl_task = tasks.skl_task(institute)
    #clg_task = tasks.clg_task(institute)
    #tour_task = tasks.tour_task(tour)
    #stay_suggest = tasks.stay_suggest(room_analyst)

    # Create crew
    print(f"Setting up crew for {city}...")
    crew = Crew(
        agents=[
            holy_places,
            #jewellery_shop,
            shopping_mart,
            #courier_service,
            #restaurant_analyst,
            #servicecenter_finder,
            #Homeapplst_finder,
            #entertainment_agent,
            #vessel_shop_agent,
            #stationary_shop_agent,
            #photoshop_agent,
            #hospital_analyst,
            #companies,
            #furniture_shop,
            #gift_shop,
            #textile,
            #parlour,
            #institute,
            #tour,
            #room_analyst
        ],
        tasks=[
            holy_place_searcher,
            #Jewellery_finder,
            mart_seracher,
            #courier_finder,
            #restaurant_suggest,
            #suggest_auto,
            #suggest_homeappl,
            #entertainment_task,
            #vessel_shop_task,
            #stationary_shop_task,
            #photoshop_task,
            #hospital_suggester,
            #finding_IT_companies,
            #finding_Automobiles_companies,
            #locating_display_furniture,
            #discovering_gift_shops,
            #text_task,
            #par_task,
            #skl_task,
            #clg_task,
            #tour_task,
            #stay_suggest
        ],
        verbose=True
    )

    # Execute crew
    print(f"\nStarting service location search for {city}...")
    print("This may take several minutes as the AI agents search for information...\n")
    
    try:
        result = crew.kickoff(inputs={"city": city})
        print("\n" + "="*80)
        print(f"RESULTS FOR {city.upper()}")
        print("="*80)
        print(result)
    except Exception as e:
        print(f"\nAn error occurred: {str(e)}")
        print("Please check your API keys and internet connection.")

if __name__ == "__main__":
    main()
