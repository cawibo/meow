use std::io::{self, BufRead};

fn main() {
	let stdin =  io::stdin();
	for line in stdin.lock().lines().skip(1).map(|l| l.unwrap()) {
		let mut nums: Vec<i64> = line.split_whitespace()
			.map(|num| num.parse().unwrap())
			.collect::<Vec<i64>>();
		nums.sort();
		// println!("{:?}", nums);

		let mut solutions = 0;

		for i in 0..nums.len() {
			for j in i+1..nums.len() {
				let ai = nums[i];
				let aj = nums[j];

				if &(ai + aj) > nums.last().unwrap() {
					continue;
				};

				// println!("testing {} and {}, sum is {}", i, j, ai+aj);

				match nums.binary_search(&(ai+aj)) {
					Ok(mut k) => {
						// back up until first occurence
						while k > 0 && nums[k-1] == ai+aj {
							k -= 1;
						}
						// println!("found sum at {:?}", k);
						while k < nums.len() && nums[k] == ai+aj {
							// println!("k: {}, ak: {}", k, nums[k]);
							if i != j && j != k && i != k {
								// println!("{} {} {}", i, j, k);
								solutions += 2;
							};
							k += 1;

						}
					},
					Err(_) => ()
				};

				// println!("");

			}
		};

		println!("{}", solutions);
	};
}