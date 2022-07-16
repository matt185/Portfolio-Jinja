const toLower = text => {
  return text.toString().toLowerCase();
};

const searchByTech = (items, term) => {
  return items.filter(item => toLower(item.techStack).includes(toLower(term)));
};

module.exports = searchByTech
