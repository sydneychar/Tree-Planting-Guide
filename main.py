from drafter import *
from dataclasses import dataclass


@dataclass
class Tree:
    name: str
    sunlight: str
    soil_type: str
    water: str
    favorite: bool
    notes: str


@dataclass
class State:
    selected_tree: str
    search_query: str
    planting_zone: str
    favorites_count: int
    trees: list[Tree]



START_TREES = [
    Tree("Red Maple", "Full Sun", "Loamy", "Medium", False, ""),
    Tree("White Oak", "Full Sun", "Well Drained", "Low", False, ""),
    Tree("River Birch", "Partial Sun", "Moist", "High", False, ""),
    Tree("Eastern Redbud", "Full Sun", "Loamy", "Medium", False, ""),
    Tree("Dogwood", "Partial Sun", "Rich Soil", "Medium", False, ""),
    Tree("Sugar Maple", "Full Sun", "Loamy", "Medium", False, ""),
    Tree("American Elm", "Full Sun", "Well Drained", "Medium", False, ""),
    Tree("Tulip Poplar", "Full Sun", "Moist", "High", False, ""),
    Tree("Southern Magnolia", "Full Sun", "Acidic", "Medium", False, ""),
    Tree("Japanese Maple", "Partial Sun", "Well Drained", "Medium", False, ""),
    Tree("Colorado Blue Spruce", "Full Sun", "Well Drained", "Low", False, ""),
    Tree("Weeping Willow", "Full Sun", "Wet", "High", False, ""),
    Tree("Bald Cypress", "Full Sun", "Wet", "Medium", False, ""),
    Tree("Black Cherry", "Full Sun", "Loamy", "Medium", False, ""),
    Tree("Northern Red Oak", "Full Sun", "Well Drained", "Low", False, ""),
    Tree("Silver Maple", "Full Sun", "Moist", "Medium", False, ""),
    Tree("Flowering Crabapple", "Full Sun", "Well Drained", "Medium", False, ""),
    Tree("Green Ash", "Full Sun", "Loamy", "Medium", False, ""),
    Tree("Ponderosa Pine", "Full Sun", "Well Drained", "Low", False, ""),
    Tree("American Sycamore", "Full Sun", "Moist", "High", False, "")
]

def find_tree(state: State):
    """returns the currently selected tree from the tree list"""
    for tree in state.trees:
        if tree.name == state.selected_tree:
            return tree
    return None


@route
def index(state: State) -> Page:
    """displays the home page and main navigation menu"""
    return Page(state, [
        "# Tree Planting Guide",

        "\nWelcome to the Tree Planting Guide!",

        "\nThis site helps gardeners find trees and learn how to care for them.\n",

        Button("Tree Library", tree_library),
        Button("Favorites", favorites),
        Button("Zone Recommendations", zone_recommendations)
    ])


@route
def tree_library(state: State) -> Page:
    """displays all 20 trees available in tree library"""
    content = []
    content.append("# Tree Library\n")

    
    for tree in state.trees:
        content.append(tree.name + "\n")

    content.append(Button("View Red Maple", red_maple))
    content.append(Button("View White Oak", white_oak))
    content.append(Button("View River Birch", river_birch))
    content.append(Button("Dogwood", dogwood))
    content.append(Button("Eastern Redbud", eastern_redbud))
    content.append(Button("Sugar Maple", sugar_maple))
    content.append(Button("American Elm", american_elm))
    content.append(Button("Tulip Poplar", tulip_poplar))
    content.append(Button("Southern Magnolia", magnolia))
    content.append(Button("Japanese Maple", japanese_maple))
    content.append(Button("Colorado Blue Spruce", blue_spruce))
    content.append(Button("Weeping Willow", weeping_willow))
    content.append(Button("Bald Cypress", bald_cypress))
    content.append(Button("Black Cherry", black_cherry))
    content.append(Button("Northern Red Oak", northern_red_oak))
    content.append(Button("Silver Maple", silver_maple))
    content.append(Button("Flowering Crabapple", flowering_crabapple))
    content.append(Button("Green Ash", green_ash))
    content.append(Button("Ponderosa Pine", ponderosa_pine))
    content.append(Button("American Sycamore", american_sycamore))

    content.append(Button("Home", index))

    return Page(state, content)


@route
def red_maple(state: State) -> Page:
    """"this selects the red maple tree and
    displays its information page"""
    state.selected_tree = "Red Maple"
    return tree_info(state)


@route
def white_oak(state: State) -> Page:
    """"this selects the white oak tree and
    displays its information page"""
    state.selected_tree = "White Oak"
    return tree_info(state)


@route
def river_birch(state: State) -> Page:
    """"this selects the river birch tree and
    displays its information page"""
    state.selected_tree = "River Birch"
    return tree_info(state)

@route
def dogwood(state: State) -> Page:
    """"this selects the dogwood tree and
    displays its information page"""
    state.selected_tree = "Dogwood"
    return tree_info(state)

@route
def eastern_redbud(state: State) -> Page:
    """"this selects the eastern redbud tree and
    displays its information page"""
    state.selected_tree = "Eastern Redbud"
    return tree_info(state)

@route
def sugar_maple(state: State) -> Page:
    """"this selects the sugar maple tree and
    displays its information page"""
    state.selected_tree = "Sugar Maple"
    return tree_info(state)

@route
def american_elm(state: State) -> Page:
    """this selects the american elm tree and
    displays its information page"""
    state.selected_tree = "American Elm"
    return tree_info(state)

@route
def tulip_poplar(state: State) -> Page:
    """"this selects the tulip poplar tree and
    displays its information page"""
    state.selected_tree = "Tulip Poplar"
    return tree_info(state)

@route
def magnolia(state: State) -> Page:
    """"this selects the southern magnolia tree and
    displays its information page"""
    state.selected_tree = "Southern Magnolia"
    return tree_info(state)

@route
def japanese_maple(state: State) -> Page:
    """"this selects the japanese maple tree and
    displays its information page"""
    state.selected_tree = "Japanese Maple"
    return tree_info(state)

@route
def blue_spruce(state: State) -> Page:
    """"this selects the colorado blue spruce tree and
    displays its information page"""
    state.selected_tree = "Colorado Blue Spruce"
    return tree_info(state)

@route
def weeping_willow(state: State) -> Page:
    """"this selects the weeping willow tree and
    displays its information page"""
    state.selected_tree = "Weeping Willow"
    return tree_info(state)

@route
def bald_cypress(state: State) -> Page:
    """"this selects the bald cypress tree and
    displays its information page"""
    state.selected_tree = "Bald Cypress"
    return tree_info(state)

@route
def black_cherry(state: State) -> Page:
    """"this selects the black cherry tree and
    displays its information page"""
    state.selected_tree = "Black Cherry"
    return tree_info(state)

@route
def northern_red_oak(state: State) -> Page:
    """"this selects the northern red oak tree and
    displays its information page"""
    state.selected_tree = "Northern Red Oak"
    return tree_info(state)

@route
def silver_maple(state: State) -> Page:
    """"this selects the silver maple tree and
    displays its information page"""
    state.selected_tree = "Silver Maple"
    return tree_info(state)

@route
def flowering_crabapple(state: State) -> Page:
    """"this selects the flowering crabapple tree and
    displays its information page"""
    state.selected_tree = "Flowering Crabapple"
    return tree_info(state)

@route
def green_ash(state: State) -> Page:
    """"this selects the green ash tree and
    displays its information page"""
    state.selected_tree = "Green Ash"
    return tree_info(state)

@route
def ponderosa_pine(state: State) -> Page:
    """"this selects the ponderosa pine tree and
    displays its information page"""
    state.selected_tree = "Ponderosa Pine"
    return tree_info(state)

@route
def american_sycamore(state: State) -> Page:
    """"this selects the american sycamore tree and
    displays its information page"""
    state.selected_tree = "American Sycamore"
    return tree_info(state)

@route
def tree_info(state: State) -> Page:
    """ displays detailed info about selected tree"""
    tree = find_tree(state)

    if tree is None:
        return index(state)

    favorite_text = "No"

    # IF STATEMENT #1
    if tree.favorite:
        favorite_text = "Yes"

    return Page(state, [
        "# Tree Information",

        "\nName: " + tree.name,
        "\nSunlight: " + tree.sunlight,
        "\nSoil Type: " + tree.soil_type,
        "\nWater Needs: " + tree.water,
        "\nFavorite: " + favorite_text,

        Button("Add Favorite", add_favorite),

        Button("Remove Favorite", remove_favorite),

        Button("Planting Instructions",
               planting_instructions),

        Button("Care Tips",
               care_tips),

        Button("Back",
               tree_library)
    ])


@route
def planting_instructions(state: State) -> Page:
    """ displays general instructions for selected tree"""
    return Page(state, [
        "# Planting Instructions",

        "\n1. Dig a hole twice as wide as the root ball.",

        "\n2. Place the tree in the hole.",

        "\n3. Fill with soil.",

        "\n4. Water thoroughly.",

        "\n5. Apply mulch.",

        Button("Back", tree_info)
    ])


@route
def care_tips(state: State) -> Page:
    """Displays basic care and maintenance tips for trees"""
    return Page(state, [
        "# Care Tips",

        "\n• Water regularly",
        "\n• Keep weeds away",
        "\n• Add mulch yearly",
        "\n• Prune dead branches",

        Button("Back", tree_info)
    ])


@route
def add_favorite(state: State) -> Page:
    """this function adds the tree to your favorites"""

    tree = find_tree(state)

    if tree is not None:

        # IF STATEMENT #2
        if not tree.favorite:

            tree.favorite = True

            state.favorites_count += 1

    return tree_info(state)


@route
def remove_favorite(state: State) -> Page:
    """this function removes the tree from your favorites"""

    tree = find_tree(state)

    if tree is not None:

        # IF STATEMENT #3
        if tree.favorite:

            tree.favorite = False

            state.favorites_count -= 1

    return tree_info(state)

from typing import Any

@route
def favorites(state: State) -> Page:
    """this will show you a list of trees that are in your
favorites"""

    content: list[Any] = ["# Favorite Trees","\nFavorites Count:"+ str(state.favorites_count) + "\n"]

    found = False


    for tree in state.trees:
        if tree.favorite:

            content.append(tree.name + "\n")

            found = True

    if not found:
        content.append("No favorite trees selected.\n")

    content.append(Button("Home", index))

    return Page(state, content)


@route
def zone_recommendations(state: State) -> Page:
    """ these zones are the USDA average annual
minimum temperature"""

    recommendation = ""

    if state.planting_zone == "Zone 4":
        recommendation = "River Birch"

    elif state.planting_zone == "Zone 5":
        recommendation = "White Oak"

    else:
        recommendation = "Red Maple"

    return Page(state, [
        "# Zone Recommendations",

        "\nCurrent Zone: "
        + state.planting_zone,

        "\nRecommended Tree: "
        + recommendation,

        Button("Zone 4", set_zone4),

        Button("Zone 5", set_zone5),

        Button("Zone 6", set_zone6),

        Button("Home", index)])


@route
def set_zone4(state: State) -> Page:
    """30°F to -20°F (-34°C to -29°C)"""
    state.planting_zone = "Zone 4"
    return zone_recommendations(state)


@route
def set_zone5(state: State) -> Page:
    """-20°F to -10°F (-29°C to -23°C)"""
    state.planting_zone = "Zone 5"
    return zone_recommendations(state)


@route
def set_zone6(state: State) -> Page:
    """-10°F to 0°F (-23°C to -18°C)"""
    state.planting_zone = "Zone 6"
    return zone_recommendations(state)

set_site_information(
    "Tree Planting Guide",
    "A guide for selecting and caring for trees.",
    "Your Name")

start_server(State( "","","Zone 5",0,START_TREES))

