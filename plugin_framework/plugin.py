class Plugin:
    def __init__(self, spec):
        self._spec = spec

    @property
    def symbolic_name(self):
        return self._spec.get("symbolic_name", "ac.rs.singidunum.name")

    @symbolic_name.setter
    def symbolic_name(self, value):
        self._spec["symbolic_name"] = value
    
    @property
    def name(self):
        return self._spec.get("name", "")

    @name.setter
    def name(self, value):
        self._spec["name"] = value
    
    @property
    def size(self):
        return self._spec.get("size", 0)

    @size.setter
    def size(self, value):
        self._spec["size"] = value
    
    @property
    def category(self):
        return self._spec.get("category", "cat1")

    @category.setter
    def category(self, value):
        self._spec["category"] = value

    @property
    def version(self):
        return self._spec.get("version", "1.0.0")
    
    @version.setter
    def version(self, value):
        self._spec["version"] = value

    @property
    def enabled(self):
        return self._spec.get("enabled", False)

    @enabled.setter
    def enabled(self, value):
        self._spec["enabled"] = value

    @property
    def description(self):
        return self._spec.get("description", "")
    
    @description.setter
    def description(self, value):
        self._spec["description"] = value
    
