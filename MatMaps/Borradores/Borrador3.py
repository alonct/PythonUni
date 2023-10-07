import MatMaps.MatMaps_code.Map_related.Points_of_Interest as P


def main():
    restaurante = P.Restaurant("Alaola", "Calle Peroniño", "Cartagena")
    print(restaurante)
    restaurante.print_gps_info()
    parking = P.Parking("Pepe", False, None, 5, "Calle Peroniño", "Cartagena")
    print(parking)
    parking.print_gps_info()
    hotel = P.Hotel("Carlos III")
    print(hotel)
    monumento = P.CultureSite("Grazzia")
    print(monumento)
    bus = P.BusStop("Canteras")
    print(bus)
    taxi = P.TaxiStop("Cartagena")
    print(taxi)
    aeropuerto = P.Airport()
    print(aeropuerto)
    gasolinera = P.GasStation()
    print(gasolinera)


if __name__ == "__main__":
    main()
