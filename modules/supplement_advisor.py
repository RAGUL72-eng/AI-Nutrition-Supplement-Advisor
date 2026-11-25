SUPPLEMENTS = {
    "Protein powder": {
        "summary": "Protein powder is a convenient way to add protein when food alone does not meet your needs. Whey comes from milk; plant blends may use pea, soy, or other proteins.",
        "cautions": "Check ingredients and allergens (especially milk/soy). It is optional, not a replacement for balanced meals. People with kidney disease should ask their clinician about protein needs."
    },
    "Creatine monohydrate": {
        "summary": "Creatine monohydrate is one of the most researched sports supplements and may support repeated high-intensity exercise and strength training when paired with training.",
        "cautions": "Choose a quality-tested product. Some people notice water-weight gain or stomach upset. Ask a clinician if you have kidney concerns or take medications."
    },
    "Vitamin D": {
        "summary": "Vitamin D supports bone health and normal muscle function. Sun exposure, foods, and supplements can contribute to intake.",
        "cautions": "High doses can be harmful. Testing and supplementation decisions should be discussed with a healthcare professional."
    },
    "Vitamin B12": {
        "summary": "Vitamin B12 supports nerve function and red blood cell formation. It is especially important to plan for adequate intake on vegan diets.",
        "cautions": "If you have symptoms or a suspected deficiency, seek medical advice and appropriate testing rather than self-treating."
    },
    "Omega-3": {
        "summary": "Omega-3 fats are found in fatty fish and some plant foods such as flaxseed, chia, and walnuts. Supplements may be considered when dietary intake is low.",
        "cautions": "Discuss supplements with a clinician if you take blood-thinning medicines, have a bleeding disorder, or are preparing for surgery."
    },
    "Electrolytes": {
        "summary": "Electrolyte drinks may be useful during prolonged exercise, heavy sweating, or heat exposure. For many everyday workouts, water and normal meals are sufficient.",
        "cautions": "Some products contain high amounts of sugar or sodium. People with kidney, heart, or blood-pressure conditions should ask a clinician."
    },
    "Caffeine": {
        "summary": "Caffeine can increase alertness and may improve exercise performance for some adults. Sensitivity varies widely.",
        "cautions": "Can affect sleep, anxiety, heart rate, and blood pressure. Avoid combining multiple stimulant products. Not suitable for everyone, including many minors and pregnant people."
    },
    "Iron": {
        "summary": "Iron is needed to make hemoglobin and carry oxygen. Iron supplements are usually best taken when a deficiency or need has been assessed.",
        "cautions": "Too much iron can be dangerous. Do not take high-dose iron without professional guidance and appropriate testing."
    },
}

def get_supplement_info(name):
    return SUPPLEMENTS.get(name, {
        "summary": "Information is not available for this item.",
        "cautions": "Ask a qualified healthcare professional before using supplements."
    })
