---
layout: default
title: Open vSwitch Commands
parent: Wiki
---

# Open vSwitch Commands
{: .no_toc }

## Table of contents
{: .no_toc .text-delta }

- TOC
{:toc}

---

## Open vSwitch Commands

- Add a flow rule (forward packets coming from port X to port Y)

```
sudo ovs-ofctl add-flow ovsbr0 in_port=X,actions=output:Y
```

- Get flow rules

```
sudo ovs-ofctl dump-flows ovsbr0
```

- Delete flow rules

```
sudo ovs-ofctl del-flows ovsbr0
```

- Get port-to-interface mappings

```
sudo ovs-ofctl show ovsbr0
```