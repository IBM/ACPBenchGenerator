(define (problem depot-2-2-2-4-4-2) (:domain depots)
(:objects
	depot0 depot1 - Depot
	distributor0 distributor1 - Distributor
	truck0 truck1 - Truck
	pallet0 pallet1 pallet2 pallet3 - Pallet
	crate0 crate1 - Crate
	hoist0 hoist1 hoist2 hoist3 - Hoist)
(:init
	(at pallet0 depot0)
	(clear crate0)
	(at pallet1 depot1)
	(clear pallet1)
	(at pallet2 distributor0)
	(clear pallet2)
	(at pallet3 distributor1)
	(clear crate1)
	(at truck0 distributor0)
	(at truck1 depot0)
	(at hoist0 depot0)
	(available hoist0)
	(at hoist1 depot1)
	(available hoist1)
	(at hoist2 distributor0)
	(available hoist2)
	(at hoist3 distributor1)
	(available hoist3)
	(at crate0 depot0)
	(on crate0 pallet0)
	(at crate1 distributor1)
	(on crate1 pallet3)
)

(:goal (and
		(on crate0 crate1)
		(on crate1 pallet0)
	)
))
